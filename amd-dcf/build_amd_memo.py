#!/usr/bin/env python3
"""
AMD DCF — Equity Research Initiating Coverage Note (PDF)
Output: AMD_DCF_Initiation_Note.pdf
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.colors import HexColor

DIR    = "/Users/paco/career/modeling-portfolio/amd-dcf"
OUTPUT = os.path.join(DIR, "AMD_DCF_Initiation_Note.pdf")
os.makedirs(DIR, exist_ok=True)

# ── Colors ─────────────────────────────────────────────────────────────────────
NAVY    = HexColor("#1F3864")
BLUE    = HexColor("#2E75B6")
TEAL    = HexColor("#17375E")
LGRAY   = HexColor("#F5F5F5")
MGRAY   = HexColor("#D6DCE4")
DGRAY   = HexColor("#595959")
BLACK   = HexColor("#1F1F1F")
GREEN   = HexColor("#375623")
RED     = HexColor("#C00000")
GOLD    = HexColor("#BF8F00")
WHITE   = colors.white

# ── Styles ─────────────────────────────────────────────────────────────────────
def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=9, leading=13, textColor=BLACK,
                spaceAfter=3, spaceBefore=0, alignment=TA_LEFT)
    base.update(kw)
    return ParagraphStyle(name, **base)

title_s   = S("title",  fontName="Helvetica-Bold", fontSize=16, textColor=NAVY,
               leading=20, spaceAfter=2)
sub_s     = S("sub",    fontSize=8, textColor=DGRAY, leading=11)
hdr_s     = S("hdr",    fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
               leading=10, alignment=TA_LEFT)
body_s    = S("body",   fontSize=8.5, leading=13, textColor=BLACK,
               alignment=TA_JUSTIFY, spaceAfter=5)
bullet_s  = S("bullet", fontSize=8.5, leading=13, leftIndent=10,
               firstLineIndent=-10, spaceAfter=2, alignment=TA_JUSTIFY)
label_s   = S("label",  fontName="Helvetica-Bold", fontSize=8, textColor=NAVY)
small_s   = S("small",  fontSize=7, textColor=DGRAY, leading=9)
rating_s  = S("rating", fontName="Helvetica-Bold", fontSize=11, textColor=WHITE,
               alignment=TA_CENTER, leading=14)
num_s     = S("num",    fontName="Helvetica-Bold", fontSize=9, textColor=NAVY,
               alignment=TA_RIGHT)
sect_s    = S("sect",   fontName="Helvetica-Bold", fontSize=8.5, textColor=WHITE,
               leading=11)

def bl(items): return [Paragraph("▪  " + i, bullet_s) for i in items]

# ── Table style helpers ─────────────────────────────────────────────────────────
def ts(*cmds):
    base = [
        ("FONT",      (0,0),(-1,-1), "Helvetica", 8),
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[WHITE, LGRAY]),
        ("GRID",      (0,0),(-1,-1), 0.3, MGRAY),
        ("VALIGN",    (0,0),(-1,-1), "MIDDLE"),
        ("TOPPADDING",(0,0),(-1,-1), 3),
        ("BOTTOMPADDING",(0,0),(-1,-1), 3),
        ("LEFTPADDING",(0,0),(-1,-1), 5),
        ("RIGHTPADDING",(0,0),(-1,-1), 5),
    ]
    base.extend(cmds)
    return TableStyle(base)

def section_bar(text):
    data = [[Paragraph(text, sect_s)]]
    t = Table(data, colWidths=[7.0*inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0),(-1,-1), TEAL),
        ("TOPPADDING", (0,0),(-1,-1), 5),
        ("BOTTOMPADDING",(0,0),(-1,-1), 5),
        ("LEFTPADDING",(0,0),(-1,-1), 8),
    ]))
    return t

# ── Document ───────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=letter,
    leftMargin=0.75*inch, rightMargin=0.75*inch,
    topMargin=0.65*inch, bottomMargin=0.65*inch,
)

story = []

# ── Header bar ─────────────────────────────────────────────────────────────────
hdr_data = [[Paragraph("EQUITY RESEARCH  |  INITIATING COVERAGE", hdr_s),
             Paragraph("SEMICONDUCTORS & SEMICONDUCTOR EQUIPMENT", hdr_s),
             Paragraph("February 2026", hdr_s)]]
hdr_tbl = Table(hdr_data, colWidths=[2.8*inch, 2.8*inch, 1.4*inch])
hdr_tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), NAVY),
    ("TOPPADDING",(0,0),(-1,-1), 5),
    ("BOTTOMPADDING",(0,0),(-1,-1), 5),
    ("LEFTPADDING",(0,0),(-1,-1), 8),
    ("RIGHTPADDING",(0,0),(-1,-1), 8),
    ("ALIGN",(2,0),(2,0),"RIGHT"),
]))
story.append(hdr_tbl)
story.append(Spacer(1, 8))

# ── Title block ────────────────────────────────────────────────────────────────
story.append(Paragraph("Advanced Micro Devices, Inc.  (NASDAQ: AMD)", title_s))
story.append(Paragraph(
    "Last Standing Challenger · Data Center GPU Ramp + Intel CPU Share Gains Drive Re-Rating",
    S("tagline", fontName="Helvetica-Oblique", fontSize=9.5, textColor=TEAL, leading=13)))
story.append(Spacer(1, 6))

# ── Rating / Stats strip ───────────────────────────────────────────────────────
rating_data = [
    [Paragraph("OVERWEIGHT", rating_s),
     Paragraph("PRICE TARGET\n$145", rating_s),
     Paragraph("CURRENT PRICE\n$120¹", rating_s),
     Paragraph("UPSIDE\n+20.8%", rating_s)],
]
rating_tbl = Table(rating_data, colWidths=[1.5*inch, 1.75*inch, 1.75*inch, 2.0*inch])
rating_tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(0,0), NAVY),
    ("BACKGROUND",(1,0),(1,0), BLUE),
    ("BACKGROUND",(2,0),(2,0), TEAL),
    ("BACKGROUND",(3,0),(3,0), GREEN),
    ("TOPPADDING",(0,0),(-1,-1), 7),
    ("BOTTOMPADDING",(0,0),(-1,-1), 7),
    ("ALIGN",(0,0),(-1,-1),"CENTER"),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
    ("GRID",(0,0),(-1,-1), 0.5, WHITE),
]))
story.append(rating_tbl)
story.append(Spacer(1, 10))

# ── Key stats grid ─────────────────────────────────────────────────────────────
stats = [
    ["Fiscal Year End", "December",        "FY2024A Revenue",  "$25.8B"],
    ["Shares Outstanding","1,620M",        "FY2024A EBITDA",   "$4.2B (GAAP)"],
    ["Market Cap (approx)","~$194B",       "FY2029E Revenue",  "$58.7B (base)"],
    ["Enterprise Value","~$190B",          "FY2029E EBITDA M", "29.0% (base)"],
    ["Net Cash",        "~$4.0B",          "Base Case WACC",   "9.0%"],
    ["NTM P/E (non-GAAP)","~27x",          "Terminal Growth",  "3.5%"],
]
def stat_tbl(rows):
    data = []
    for r in rows:
        data.append([
            Paragraph(r[0], S("sl", fontSize=8, textColor=DGRAY)),
            Paragraph(r[1], S("sv", fontName="Helvetica-Bold", fontSize=8, textColor=NAVY, alignment=TA_RIGHT)),
            Paragraph(r[2], S("sl2", fontSize=8, textColor=DGRAY)),
            Paragraph(r[3], S("sv2", fontName="Helvetica-Bold", fontSize=8, textColor=NAVY, alignment=TA_RIGHT)),
        ])
    t = Table(data, colWidths=[1.6*inch, 1.15*inch, 1.75*inch, 1.15*inch])
    t.setStyle(TableStyle([
        ("ROWBACKGROUNDS",(0,0),(-1,-1),[WHITE, LGRAY]),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("LINEBELOW",(0,-1),(-1,-1),0.5,MGRAY),
    ]))
    return t

story.append(stat_tbl(stats))
story.append(Spacer(1, 10))

# ── Executive Summary ──────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("EXECUTIVE SUMMARY"),
    Spacer(1, 5),
    Paragraph(
        "We initiate coverage of Advanced Micro Devices (AMD) with an <b>Overweight</b> rating and "
        "a <b>$145 price target</b>, implying 20.8% upside from current levels. AMD sits at the "
        "intersection of two secular shifts: the collapse of Intel's CPU dominance and the explosion "
        "in AI accelerator demand. Our 5-year DCF (WACC: 9.0%, TGR: 3.5%) models 17.9% revenue CAGR "
        "and EBITDA margin expansion from 21.6% (FY2024A) to 29.0% (FY2029E) as revenue mix shifts "
        "toward high-margin Data Center.", body_s),
    Paragraph(
        "The key debate is simple: can AMD's MI300X/MI350/MI400 series take meaningful AI accelerator "
        "share from Nvidia? We don't need AMD to beat Nvidia — we just need AMD to be relevant. At "
        "$120, the market is pricing in modest success. Our base case assumes 28% Data Center revenue "
        "CAGR, implying AMD holds 10–12% of the AI accelerator TAM by FY2029. That is conservative "
        "relative to AMD's current MI300X design wins at Microsoft, Meta, and Oracle.", body_s),
]))
story.append(Spacer(1, 8))

# ── Investment Thesis ──────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("INVESTMENT THESIS — FOUR VALUE CREATION DRIVERS"),
    Spacer(1, 5),
]))

drivers = [
    ("1.  Data Center GPU Ramp",
     "The MI300X launched in Q4 2023 as the first legitimate alternative to Nvidia's H100 in "
     "large language model inference workloads — where memory bandwidth matters more than raw "
     "FLOPS. With 192GB HBM3 vs. Nvidia's 80GB, AMD wins on memory-intensive inference tasks. "
     "MI300X already powers Azure's GPT-4o inference fleet and Meta's Llama 3 serving. We model "
     "Data Center at $38.3B by FY2029, a 25% CAGR from FY2024's $12.6B."),
    ("2.  Intel CPU Share Gains",
     "Intel's manufacturing stumbles — delayed 10nm, botched Sapphire Rapids, CEO turnover — "
     "handed AMD structural server CPU share. AMD EPYC now runs in 4 of 5 major hyperscalers and "
     "holds ~35% server CPU market share, up from near zero in 2017. Each 1% of server CPU share "
     "is worth ~$400M in annual revenue. Client Ryzen continues gaining in premium notebooks."),
    ("3.  Operating Leverage & Amortization Roll-Off",
     "AMD's fabless model means Data Center revenue scales at 65–70% gross margin with minimal "
     "incremental capex (~$300–600M/yr vs. Intel's $20B+ capex). Equally important: AMD's GAAP "
     "results are depressed by ~$3.8B/yr in Xilinx acquisition amortization (acquired Feb 2022 "
     "for $49B). As this rolls off toward FY2028–FY2029, GAAP EPS will reconnect with cash "
     "earnings — a re-rating catalyst most generalist investors haven't modeled."),
    ("4.  Embedded Recovery (Xilinx FPGAs)",
     "AMD's Embedded segment collapsed from $5.3B (FY2023) to $3.6B (FY2024) as customers burned "
     "through excess FPGA inventory. Recovery is underway. Xilinx FPGAs dominate aerospace, "
     "defense, automotive, and telecom — all industries with zero-tolerance for supplier switches. "
     "We model 25% Embedded growth in FY2025E as inventory digestion completes, reaching $6.9B "
     "by FY2029."),
]
for title, desc in drivers:
    story.append(KeepTogether([
        Paragraph(f"<b>{title}</b>", S("dh", fontSize=8.5, textColor=NAVY, spaceAfter=2)),
        Paragraph(desc, body_s),
        Spacer(1, 3),
    ]))

# ── Financial Projections ──────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("FINANCIAL PROJECTIONS  ($M, FY ending December)"),
    Spacer(1, 5),
]))

fin_hdr = ["Metric", "FY2022A", "FY2023A", "FY2024A", "FY2025E", "FY2026E", "FY2027E", "FY2028E", "FY2029E"]
fin_data = [
    fin_hdr,
    ["Revenue",       "23,601", "22,680", "25,785", "32,188", "39,725", "47,165", "53,655", "58,673"],
    ["  YoY Growth",       "—",      "—",  "+13.7%", "+24.8%", "+23.4%", "+18.7%", "+13.8%",  "+9.3%"],
    ["Gross Profit",   "10,492", "10,460", "12,382", "16,094", "20,657", "25,469", "29,778", "33,444"],
    ["  Gross Margin",  "44.5%",  "46.1%",  "48.0%",  "50.0%",  "52.0%",  "54.0%",  "55.5%",  "57.0%"],
    ["EBITDA",          "3,937",  "4,338",  "5,569",  "6,920",  "9,733", "12,499", "15,023", "17,015"],
    ["  EBITDA Margin",  "16.7%",  "19.1%",  "21.6%",  "21.5%",  "24.5%",  "26.5%",  "28.0%",  "29.0%"],
    ["D&A",             "3,936",  "3,936",  "3,758",  "3,700",  "3,400",  "3,100",  "2,750",  "2,400"],
    ["EBIT (GAAP)",        "1",    "402",    "1,811",  "3,220",  "6,333",  "9,399", "12,273", "14,615"],
    ["Unlevered FCF",     "N/M",     "N/M",    "N/M",  "5,737",  "7,908", "10,139", "12,257", "13,873"],
]

def fin_table(rows):
    col_w = [1.55*inch] + [0.74*inch]*8
    data_p = []
    for i, row in enumerate(rows):
        pr = []
        for j, cell in enumerate(row):
            is_hdr = (i == 0)
            is_sub = (not is_hdr and cell.startswith("  "))
            bold = is_hdr or (not is_sub and j == 0)
            color = WHITE if is_hdr else (DGRAY if is_sub else (NAVY if j == 0 else BLACK))
            align = TA_RIGHT if j > 0 else TA_LEFT
            style = ParagraphStyle("fc", fontName="Helvetica-Bold" if bold else "Helvetica",
                                   fontSize=7.5, textColor=color, alignment=align,
                                   leading=10)
            pr.append(Paragraph(cell.strip(), style))
        data_p.append(pr)
    t = Table(data_p, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, LGRAY]),
        ("LINEBELOW",(0,0),(-1,0), 1, NAVY),
        ("LINEBELOW",(0,-1),(-1,-1), 0.5, NAVY),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),4),("RIGHTPADDING",(0,0),(-1,-1),4),
        ("LINEAFTER",(2,0),(2,-1), 0.75, BLUE),  # divider: hist vs projected
    ]))
    return t

story.append(fin_table(fin_data))
story.append(Spacer(1, 8))

# ── DCF Returns ────────────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("DCF RETURNS ANALYSIS"),
    Spacer(1, 5),
]))

dcf_cols = ["Component", "Value", "Notes"]
dcf_rows = [
    dcf_cols,
    ["Sum of PV (FCFs, FY2025–FY2029)",  "$37,174M",  "Discounted at 9.0% WACC, mid-year convention"],
    ["Terminal Value (Gordon Growth)",    "$261,055M", "FY2029E FCF × 1.035 / (9.0% – 3.5%)"],
    ["PV of Terminal Value",             "$169,626M", "Discounted 4.5 periods at 9.0%"],
    ["Enterprise Value",                 "$206,800M", "PV FCFs + PV Terminal Value"],
    ["Plus: Cash & Equivalents",          "+$5,700M", "AMD Q4 2024 balance sheet"],
    ["Less: Total Debt",                  "–$1,700M", "Senior notes, primarily 2026 maturity"],
    ["Equity Value",                     "$210,800M", ""],
    ["Shares Outstanding",                 "1,620M",  "Fully diluted, Q4 2024"],
    ["Implied Price Per Share",              "$130",   "Base DCF output"],
    ["Bull Case (WACC 8.5%, TGR 4.0%)",     "$205",   "Data Center 40%+ CAGR, margin upside"],
    ["Bear Case (WACC 11.0%, TGR 3.0%)",     "$68",   "DC disappoints, Nvidia moat holds"],
    ["Price Target (analyst judgment)",      "$145",   "Bull-adjusted base, rounded"],
]

def dcf_tbl(rows):
    col_w = [3.0*inch, 1.2*inch, 2.8*inch]
    data_p = []
    for i, row in enumerate(rows):
        is_hdr = (i == 0)
        is_key = (not is_hdr and ("Implied" in row[0] or "Price Target" in row[0] or "Enterprise" in row[0]))
        pr = []
        for j, cell in enumerate(row):
            bold = is_hdr or is_key
            color = WHITE if is_hdr else (NAVY if is_key else BLACK)
            align = TA_CENTER if j == 1 else (TA_LEFT)
            style = ParagraphStyle("dc", fontName="Helvetica-Bold" if bold else "Helvetica",
                                   fontSize=7.5, textColor=color, alignment=align, leading=10)
            pr.append(Paragraph(cell, style))
        data_p.append(pr)
    t = Table(data_p, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), NAVY),
        ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, LGRAY]),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
        ("LINEBELOW",(0,0),(-1,0),1,NAVY),
        ("LINEBELOW",(0,-1),(-1,-1),0.5,NAVY),
        ("BACKGROUND",(0,9),(1,9), HexColor("#DBE5F1")),  # implied PT row
        ("BACKGROUND",(0,12),(1,12), HexColor("#DBE5F1")),
    ]))
    return t

story.append(dcf_tbl(dcf_rows))
story.append(Spacer(1, 8))

# ── Sensitivity Summary ────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("SENSITIVITY — WACC × TERMINAL GROWTH RATE  (Implied Share Price)"),
    Spacer(1, 5),
]))

import math
ufcf_vals = [5737, 7908, 10139, 12257, 13873]
cash = 5700; debt = 1700; shares = 1620

def dcf_price(wacc, tgr):
    pv = sum(u/(1+wacc)**(0.5+i) for i,u in enumerate(ufcf_vals))
    tv = ufcf_vals[-1]*(1+tgr)/(wacc-tgr) if wacc > tgr else 0
    pv_tv = tv/(1+wacc)**4.5
    return (pv + pv_tv + cash - debt)/shares

wacc_r = [0.075, 0.080, 0.085, 0.090, 0.095, 0.100, 0.105]
tgr_r  = [0.025, 0.030, 0.035, 0.040, 0.045]

sens_data = [["TGR \\ WACC"] + [f"{w:.1%}" for w in wacc_r]]
for tgr in tgr_r:
    row = [f"{tgr:.1%}"]
    for wacc in wacc_r:
        row.append(f"${dcf_price(wacc,tgr):,.0f}")
    sens_data.append(row)

def sens_tbl(rows):
    col_w = [0.72*inch]*8
    data_p = []
    for i, row in enumerate(rows):
        pr = []
        for j, cell in enumerate(row):
            is_hdr = (i == 0 or j == 0)
            try:
                price = float(cell.replace("$","").replace(",",""))
                color = GREEN if price >= 145 else (HexColor("#375623") if price >= 120 else (RED if price < 85 else BLACK))
                bold = price >= 145 or price < 85
            except:
                color = WHITE if is_hdr else BLACK
                bold = is_hdr
            align = TA_CENTER
            style = ParagraphStyle("sc", fontName="Helvetica-Bold" if bold else "Helvetica",
                                   fontSize=7.5, textColor=color if not is_hdr else WHITE,
                                   alignment=align, leading=10)
            pr.append(Paragraph(cell, style))
        data_p.append(pr)
    t = Table(data_p, colWidths=col_w)
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,0), NAVY),
        ("BACKGROUND",(0,0),(0,-1), TEAL),
        ("ROWBACKGROUNDS",(1,1),(-1,-1),[WHITE, LGRAY]),
        ("TOPPADDING",(0,0),(-1,-1),3),("BOTTOMPADDING",(0,0),(-1,-1),3),
        ("LEFTPADDING",(0,0),(-1,-1),3),("RIGHTPADDING",(0,0),(-1,-1),3),
        ("LINEBELOW",(0,0),(-1,0),1,NAVY),
        ("GRID",(0,0),(-1,-1),0.3,MGRAY),
    ]))
    return t

story.append(sens_tbl(sens_data))
story.append(Paragraph(
    "Green = above $145 PT  ·  Dark green = above $120 current  ·  Red = below $85  |  "
    "Base case: WACC 9.0%, TGR 3.5% (highlighted cell).",
    small_s))
story.append(Spacer(1, 8))

# ── Key Risks ──────────────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("KEY RISKS & MITIGANTS"),
    Spacer(1, 5),
]))

risks = [
    ("Nvidia CUDA Ecosystem Moat",
     "Nvidia's CUDA software stack has a 15-year head start. AMD's ROCm is catching up but "
     "enterprise AI teams default to CUDA. AMD needs hyperscalers — not enterprises — to drive "
     "initial adoption, which is already happening.",
     "AMD wins on memory bandwidth for inference; hyperscalers are actively dual-sourcing to "
     "reduce Nvidia concentration risk. Microsoft, Meta, and Oracle MI300X deployments validate "
     "the product is enterprise-ready."),
    ("Execution Risk on MI400 Roadmap",
     "Any delay in the MI400 (successor to MI300X, expected 2025) gives Nvidia time to cement "
     "Blackwell (B200/B300) dominance before AMD can respond.",
     "AMD has shipped every major product on schedule since Lisa Su took CEO in 2014. Track "
     "record is strong. MI350 is an interim bridge product already in sampling."),
    ("Semiconductor Cyclicality",
     "A global semi cycle downturn would simultaneously hit Client (Ryzen) and Embedded (Xilinx) "
     "segments, partially offsetting Data Center strength.",
     "Data Center is the largest and fastest-growing segment, providing a natural hedge. Net cash "
     "position ($4B) provides balance sheet resilience through cycles."),
    ("Valuation Multiple Risk",
     "AMD trades at ~27x NTM non-GAAP P/E — pricing in significant execution. A quarterly miss "
     "on Data Center revenue would trigger a de-rating.",
     "Our $145 PT is based on DCF, not multiple expansion. Base case uses conservative WACC (9%) "
     "and requires no multiple expansion — upside comes from operational improvement only."),
]

risks_data = [["Risk Factor", "Bear Case Scenario", "Mitigant"]]
for risk, bear, mit in risks:
    risks_data.append([
        Paragraph(f"<b>{risk}</b>", S("rn", fontSize=7.5, textColor=RED)),
        Paragraph(bear, S("rb", fontSize=7.5, leading=10)),
        Paragraph(mit, S("rm", fontSize=7.5, textColor=GREEN, leading=10)),
    ])

r_tbl = Table(risks_data, colWidths=[1.6*inch, 2.7*inch, 2.7*inch])
r_tbl.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0), NAVY),
    ("FONT",(0,0),(-1,0),"Helvetica-Bold",7.5),
    ("TEXTCOLOR",(0,0),(-1,0),WHITE),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, LGRAY]),
    ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
    ("LEFTPADDING",(0,0),(-1,-1),5),("RIGHTPADDING",(0,0),(-1,-1),5),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("LINEBELOW",(0,0),(-1,0),1,NAVY),
    ("LINEBELOW",(0,-1),(-1,-1),0.5,NAVY),
    ("GRID",(0,0),(-1,-1),0.3,MGRAY),
]))
story.append(r_tbl)
story.append(Spacer(1, 8))

# ── Recommendation ─────────────────────────────────────────────────────────────
story.append(KeepTogether([
    section_bar("RECOMMENDATION"),
    Spacer(1, 5),
    Paragraph(
        "<b>Initiate with Overweight · Price Target $145 · ~21% upside from $120.</b>",
        S("rec_hdr", fontName="Helvetica-Bold", fontSize=9, textColor=NAVY, spaceAfter=4)),
    Paragraph(
        "AMD is the only credible alternative to Nvidia in AI acceleration and the primary "
        "beneficiary of Intel's structural decline. At $120, you are paying a fair price for "
        "the base case — but getting the Data Center GPU ramp optionality for free. Our "
        "probability-weighted price target across bull/base/bear scenarios is approximately "
        "<b>$150</b>, implying 25% expected return. The risk/reward is asymmetric: bull case "
        "upside (+71%) meaningfully exceeds bear case downside (–43%), given AMD's Xilinx "
        "amortization re-rating catalyst and continued CPU share gains.", body_s),
    Paragraph(
        "Key catalysts to watch: <b>(1)</b> MI350/MI400 sampling and customer announcement, "
        "<b>(2)</b> Data Center revenue acceleration in Q1–Q2 2026 earnings calls, "
        "<b>(3)</b> Xilinx Embedded segment revenue recovery confirming inventory digestion "
        "is complete, <b>(4)</b> any Intel production setback that accelerates EPYC adoption.", body_s),
]))
story.append(Spacer(1, 10))

# ── Footnotes / Disclaimer ─────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=0.5, color=MGRAY))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "¹ Current price is a placeholder as of model build date (February 2026). Update the current "
    "price input in the DCF tab to refresh implied upside/downside.  "
    "All dollar figures in USD millions unless otherwise noted.  "
    "Historical financials sourced from AMD 10-K filings (FY2022–FY2024).  "
    "Projections represent analyst estimates and are subject to material uncertainty.  "
    "This document is for portfolio and educational purposes only and does not constitute "
    "investment advice.  Francisco Rodriguez · Dallas, TX · February 2026.",
    small_s))

# ── Build PDF ──────────────────────────────────────────────────────────────────
doc.build(story)
print(f"✓  AMD initiation note saved → {OUTPUT}")
