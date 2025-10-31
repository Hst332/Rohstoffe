import pandas as pd
from datetime import datetime
import os

# === Datenbasis ===
data = [
    ["Gold (XAU/USD)", 30, 40, 30, "Kurze Konsolidierung, schwaches Momentum.", 45, 30, 25, "Mittelfristig unterstützt durch realzinsgetriebene Nachfrage."],
    ["Silber (XAG/USD)", 35, 35, 30, "Volatil, kurzfristige Rangebildung.", 50, 30, 20, "Mittelfristig durch industrielle Nachfrage gestützt."],
    ["Kakao (Cocoa)", 50, 25, 25, "Angebotsdefizit stützt Preise.", 55, 25, 20, "Knappes Angebot hält Druck nach oben."],
    ["Kaffee (Coffee C)", 45, 35, 20, "Saisonale Stärke, Angebotsrisiko.", 50, 30, 20, "Mittelfristig weiterhin positive Tendenz."],
    ["Kupfer (Copper)", 40, 40, 20, "Kurzfristig stabil, Nachfrage verhalten.", 48, 32, 20, "Mittelfristig leicht bullish bei stabiler Industrie."],
    ["Öl (WTI)", 50, 30, 20, "Angebots- und Nachfragetreiber leicht bullish.", 52, 28, 20, "Mittelfristig durch Angebotssteuerung gestützt."],
    ["Erdgas (Natural Gas)", 40, 45, 15, "Stabil mit leichter Aufwärtstendenz.", 50, 30, 20, "Saisonal höhere Nachfrage möglich."],
    ["Baumwolle (Cotton)", 35, 45, 20, "Seitwärts; wettergetrieben.", 42, 38, 20, "Mittelfristig leicht positiv."],
    ["Zinn (Tin)", 38, 42, 20, "Kleinmarkt, Angebotsschwankungen.", 45, 35, 20, "Tech-Nachfrage kann mittelfristig treiben."],
    ["Aluminium", 36, 44, 20, "Ruhiger Verlauf, energiekostengetrieben.", 44, 36, 20, "Leichte Erholung bei stabiler Nachfrage."],
    ["Weizen (Wheat)", 42, 38, 20, "Wetterrisiko unterstützt.", 48, 32, 20, "Ernteunsicherheit bullisher Faktor."],
    ["Mais (Corn)", 40, 40, 20, "Ausgeglichen; wetterabhängig.", 46, 34, 20, "Mittelfristig Nachfrage stützend."]
]

cols = [
    "Anlageklasse",
    "1-5T_Steigt", "1-5T_Bleibt", "1-5T_Fällt", "Einschätzung_1-5T",
    "2-3W_Steigt", "2-3W_Bleibt", "2-3W_Fällt", "Einschätzung_2-3W"
]

df = pd.DataFrame(data, columns=cols)
df["Diff_1-5"] = abs(df["1-5T_Steigt"] - df["1-5T_Fällt"])
df["Diff_2-3W"] = abs(df["2-3W_Steigt"] - df["2-3W_Fällt"])
df = df.sort_values(by="Diff_1-5", ascending=False)

# === Speichern ===
date_str = datetime.now().strftime("%Y-%m-%d")
csv_name = f"commodities_probabilities_{date_str}.csv"
xlsx_name = f"commodities_probabilities_{date_str}.xlsx"
df.to_csv(csv_name, index=False)
df.to_excel(xlsx_name, index=False)

# === Markdown-Tabelle erzeugen ===
md_table = "| Anlageklasse | Steigt | Bleibt gleich | Fällt | Einschätzung (1–5 Tage) |\n"
md_table += "|---------------|---------|----------------|--------|--------------------------|\n"
for _, r in df.iterrows():
    md_table += f"| {r['Anlageklasse']} | {r['1-5T_Steigt']}% | {r['1-5T_Bleibt']}% | {r['1-5T_Fällt']}% | {r['Einschätzung_1-5T']} |\n"

readme_section = f"### 📊 Rohstoff-Wahrscheinlichkeiten (aktualisiert: {date_str})\n\n{md_table}\n"

# === README.md aktualisieren ===
readme_path = "README.md"
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
else:
    content = ""

start_tag = "<!--AUTO-TABLE-START-->"
end_tag = "<!--AUTO-TABLE-END-->"

if start_tag in content and end_tag in content:
    before = content.split(start_tag)[0]
    after = content.split(end_tag)[1]
    new_content = f"{before}{start_tag}\n{readme_section}\n{end_tag}{after}"
else:
    new_content = f"{start_tag}\n{readme_section}\n{end_tag}"

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"✅ Daten & README aktualisiert für {date_str}")
