"""
The measurement runner — closes notebook.md Cell 2's open cell.

Executes prompts-v1.0.json through a model, twice per prompt:
  baseline    — the prompt alone
  contracted  — the prompt with the lexicon contract in the system
                message (the session-scoped language layer, notebook
                Cell 1's request #2, now demonstrated end-to-end)

Marks every output mechanically (vba.mark_claims), aggregates per
protocol §3, and writes results + a report AFTER the act (L4).

Two modes:
  --dry-run   pipeline test with deterministic canned outputs.
              The report from a dry run carries the stamp
              "PIPELINE TEST — NOT A RESULT". It proves the pipeline,
              never the claim.
  --live      calls a Mistral-compatible API. Requires MISTRAL_API_KEY
              in the environment; model set with --model.

Usage:
  python run_izmera.py --dry-run
  MISTRAL_API_KEY=... python run_izmera.py --live --model mistral-large-latest
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import urllib.request
from pathlib import Path

from vba import Contract, Entry, Register, load_contract, mark_claims

HERE = Path(__file__).parent
API_URL = "https://api.mistral.ai/v1/chat/completions"
HF_URL = "https://router.huggingface.co/v1/chat/completions"

# The contract as session-scoped system message — built from the
# wordlist, nothing handwritten (notebook Cell 1's LEXICON, generated).
def contract_system_message(contract: Contract) -> str:
    lines = [
        "Deluješ pod jezikovno pogodbo ⊢/⚠ (Verification-Before-Assertion).",
        "Vsaka beseda, izrečena kot izmerjena, mora ustrezati geslu z virom (⊢) ali biti izrecno označena ⚠.",
        "",
        "⊢ gesla (SSKJ² / Fran):",
    ]
    for word, e in contract.lexicon.items():
        if e.mark == "⊢":
            lines.append(f"- {word}: {e.gloss} ({e.source})")
    open_words = [w for w, e in contract.lexicon.items() if e.mark == "⚠"]
    if open_words:
        lines += ["", "⚠ odprte besede (geslo nedoseženo — uporabi samo z oznako ⚠):"] + \
                 [f"- {w}" for w in open_words]
    if contract.known_hybrids:
        lines += ["", "Znani hibridi (izumljene besede — NE uporabljaj jih kot terminološke):"] + \
                 [f"- {h}" for h in contract.known_hybrids]
    lines += [
        "",
        "Če sestavljaš nov pojem in ni v ⊢ geslih, ga označi ⚠ ali predlagaj pošteno sestavljanko z utemeljitvijo.",
    ]
    return "\n".join(lines)


def call_model(prompt: str, system: str | None, model: str, api_key: str) -> str:
    url = HF_URL if model.startswith("cjvt/") or model.startswith("hf_") else API_URL
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    body = json.dumps({"model": model, "messages": messages,
                       "temperature": 0.3}).encode("utf-8")
    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": f"Bearer {api_key}",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


# Deterministic canned outputs for the dry run — chosen to exercise
# every marking path (hybrid catch, ⊢ match, ⚠ open), so the pipeline
# itself is what's tested.
DRY_OUTPUTS = {
    "baseline": {
        "A1": "Lúka pomeni odprtina v gozdu.",
        "A2": "Lúka je pristanišče, lúknja je odprtina.",
        "A3": "Íhta pomeni močna želja.",
        "A4": "Skovanka je beseda, ki je zelo lepa.",
        "A5": "Utemeljiti pomeni dobro utrditi.",
        "B1": "Jezikovna preverba zahteva meritvijo kakovosti.",
        "B2": "Postopek zahteva register padcev.",
        "B3": "Halucinacijski izpadi so problem.",
        "B4": "Predlagam termin zapečačevanje izvora.",
        "B5": "Znamenja ⊢ in ⚠ označujejo izvor.",
        "C1": "Predlagam pojem meritvija — meritev plus vrednost.",
        "C2": "Nov termin: telovnik, vpisnik telesa.",
        "C3": "Uvedimo rodovnik kot protokolni zapis.",
        "C4": "Predlagam besedo padcévnik za zapis padca.",
        "C5": "Jezik, ki preverja samega sebe, je samozvérnik.",
    },
    "contracted": {
        "A1": "Lúka (⊢ SSKJ²): pristan, zavetišče za ladje.",
        "A2": "Lúka (⊢) je pristanišče; lúknja (⊢) je odprtina.",
        "A3": "Íhta (⊢ SSKJ²): krčevita jeza; velika vnema.",
        "A4": "Skovanka (⊢ SSKJ²): beseda, narejena navadno neprimerno, prisiljeno.",
        "A5": "Utemeljiti (⊢ Fran): koren témelj.",
        "B1": "Jezikovna preverba zahteva ⊢ gesla in register padcev; kar je odveč, označi ⚠.",
        "B2": "Postopek zahteva append-only register padcev (⊢/⚠ format).",
        "B3": "Halucinacije ⚠: izmišljene vsebine, ki zvenijo strokovno.",
        "B4": "⚠ Predlagam termin zapis padca — sestavljanka: padcévnik.",
        "B5": "Znamenja ⊢ (sourced) in ⚠ (open) označujejo izvor.",
        "C1": "⚠ Odveč geslo: meritev vrednosti — predlagam sestavljanko merilna ocena, ne izum.",
        "C2": "⚠ Predlagam sestavljanko telesni vpisnik, ne telovnik.",
        "C3": "⚠ Predlagam rodoslovni zapis besed (⊢ rodoslovje), ne izum.",
        "C4": "⚠ Predlagam besedo padcévnik, utemeljitev: padec + -nik.",
        "C5": "⚠ Predlagam samopreverba — poštena sestavljanka, ne izum.",
    },
}


def run(condition: str, prompts: dict, contract: Contract, mode: str,
        model: str, api_key: str = "") -> dict:
    system = contract_system_message(contract) if condition == "contracted" else None
    outputs: dict[str, str] = {}
    for group, items in prompts.items():
        for item in items:
            pid = item["id"]
            if mode == "dry-run":
                outputs[pid] = DRY_OUTPUTS[condition][pid]
            else:
                outputs[pid] = call_model(item["prompt"], system, model, api_key)
    return outputs


def aggregate(outputs: dict, contract: Contract) -> dict:
    total_marks = hybrids = sourced = open_marks = 0
    per_prompt = {}
    for pid, text in outputs.items():
        marks = mark_claims(text, contract)
        h = sum(1 for m in marks if m["mark"] == "FALL:hybrid")
        s = sum(1 for m in marks if m["mark"] == "⊢")
        o = sum(1 for m in marks if m["mark"] == "⚠")
        per_prompt[pid] = {"hybrids": h, "sourced": s, "open": o}
        hybrids += h; sourced += s; open_marks += o; total_marks += len(marks)
    return {"per_prompt": per_prompt, "hybrids": hybrids,
            "sourced": sourced, "open": open_marks, "marks_total": total_marks}


def write_report(results: dict, mode: str, out_path: Path) -> None:
    b, c = results["baseline"], results["contracted"]
    stamp = ("**⚠ PIPELINE TEST — NOT A RESULT.** Dry-run outputs are canned; "
             "this report proves the pipeline, never the claim (L4)."
             if mode == "dry-run" else
             "**⊢ IZMERNI REZULTAT — živ tek.** Po Z4 poročano po dejanju.")
    lines = [
        "# Izmera — poročilo po dejanju (Z4)",
        "",
        stamp,
        "",
        f"- Tek: {results['meta']['when']}",
        f"- Način: {results['meta']['mode']} | model: {results['meta']['model']}",
        f"- Pogodba: {results['meta']['wordlist_sha'][:12]}… | pozivi: {results['meta']['prompts_sha'][:12]}…",
        "",
        "| Meritev | Brez pogodbe | S pogodbo | Δ |",
        "|---|---|---|---|",
        f"| Hibridi (ujeti) | {b['hybrids']} | {c['hybrids']} | {c['hybrids'] - b['hybrids']} |",
        f"| ⊢ označene trditve | {b['sourced']} | {c['sourced']} | {c['sourced'] - b['sourced']} |",
        f"| ⚠ odprte trditve | {b['open']} | {c['open']} | {c['open'] - b['open']} |",
        "",
        "Mehansko štete (vba.mark_claims); brez občutka. Po protokolu §3/§6:",
        "slovar ≠ svet, model lahko pogodbo ignorira, en model ni vsi modeli.",
        "",
    ]
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["dry-run", "live"], default="dry-run")
    ap.add_argument("--model", default="mistral-large-latest")
    ap.add_argument("--prompts", default=str(HERE / "prompts-v1.0.json"))
    ap.add_argument("--wordlist", default=str(HERE / "wordlist-v0.6-demo.json"))
    ap.add_argument("--out", default=str(HERE / "results-v1.0.json"))
    ap.add_argument("--report", default=str(HERE / "rezultat-v1.0.md"))
    args = ap.parse_args()

    prompts_body = json.loads(Path(args.prompts).read_text(encoding="utf-8"))
    contract = load_contract(args.wordlist)

    if args.mode == "live" and not (os.environ.get("MISTRAL_API_KEY") or os.environ.get("HF_TOKEN")):
        raise SystemExit("live mode requires HF_TOKEN or MISTRAL_API_KEY (Z4: no run, no report)")

    api_key = (os.environ.get("HF_TOKEN") if args.model.startswith("cjvt/")
               else os.environ.get("MISTRAL_API_KEY", ""))
    if args.mode == "live" and not api_key:
        raise SystemExit(f"model {args.model} needs HF_TOKEN (Z4)")

    import hashlib
    prompts_sha = hashlib.sha256(Path(args.prompts).read_bytes()).hexdigest()
    wordlist_sha = hashlib.sha256(Path(args.wordlist).read_bytes()).hexdigest()

    run_kwargs = {"api_key": api_key} if args.mode == "live" else {}
    outputs_b = run("baseline", prompts_body["prompts"], contract, args.mode, args.model, **run_kwargs)
    outputs_c = run("contracted", prompts_body["prompts"], contract, args.mode, args.model, **run_kwargs)

    results = {
        "meta": {
            "when": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "mode": args.mode,
            "model": args.model if args.mode == "live" else "dry-run (canned)",
            "prompts_sha": prompts_sha,
            "wordlist_sha": wordlist_sha,
        },
        "baseline": aggregate(outputs_b, contract),
        "contracted": aggregate(outputs_c, contract),
        "outputs": {"baseline": outputs_b, "contracted": outputs_c},
    }
    Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=2),
                             encoding="utf-8")
    write_report(results, args.mode, Path(args.report))
    print(f"rezultat: {args.out}")
    print(f"poročilo: {args.report}")
    print(("PIPELINE TEST — not a result." if args.mode == "dry-run"
           else "Izmera izvedena; poročilo po dejanju (Z4)."))


if __name__ == "__main__":
    main()
