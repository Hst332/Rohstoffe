import pandas as pd
from datetime import datetime

# === Rohstoffdaten mit geschätzten Wahrscheinlichkeiten ===
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

# Differenzen und Ranking
df["Diff_1-5"] = abs(df["1-5T_Steigt"] - df["1-5T_Fällt"])
df["Diff_2-3W"] = abs(df["2-3W_Steigt"] - df["2-3W_Fällt"])
df = df.sort_values(by="Diff_1-5", ascending=False)

# Zeitstempel
date_str = datetime.now().strftime("%Y-%m-%d")

# Speichern
df.to_csv(f"commodities_probabilities_{date_str}.csv", index=False)
df.to_excel(f"commodities_probabilities_{date_str}.xlsx", index=False)

print(f"✅ Dateien erstellt für {date_str}")
