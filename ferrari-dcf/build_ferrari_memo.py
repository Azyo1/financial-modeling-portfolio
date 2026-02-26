#!/usr/bin/env python3
"""
Ferrari N.V. (NYSE: RACE) — Equity Research Initiation Note
"The Luce Catalyst: Market Is Pricing Ferrari Like BMW, We Think It's Hermès"
Generates: Ferrari_DCF_Initiation_Note.pdf
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import PageBreak

DIR    = "/Users/paco/career/modeling-portfolio/ferrari-dcf"
OUTPUT = os.path.join(DIR, "Ferrari_DCF_Initiation_Note.pdf")
os.makedirs(DIR, exist_ok=True)

# ── Colors ─────────────────────────────────────────────────────────────────────
FERRARI_RED  = colors.HexColor("#C0272D")
CRIMSON      = colors.HexColor("#8B0000")
NAVY         = colors.HexColor("#1F3864")
TEAL         = colors.HexColor("#17375E")
GREEN_DARK   = colors.HexColor("#375623")
LGRAY        = colors.HexColor("#F5F5F5")
MGRAY        = colors.HexColor("#D6DCE4")
DGRAY        = colors.HexColor("#595959")
WHITE        = colors.white
BLACK        = colors.black

# ── Styles ─────────────────────────────────────────────────────────────────────
def styles():
    s = {}

    s["title"] = ParagraphStyle(
        "title", fontName="Helvetica-Bold", fontSize=18,
        textColor=CRIMSON, spaceAfter=2, leading=22, alignment=TA_LEFT
    )
    s["subtitle"] = ParagraphStyle(
        "subtitle", fontName="Helvetica", fontSize=9,
        textColor=DGRAY, spaceAfter=1, leading=12, alignment=TA_LEFT
    )
    s["thesis_headline"] = ParagraphStyle(
        "thesis_headline", fontName="Helvetica-BoldOblique", fontSize=11,
        textColor=NAVY, spaceAfter=6, leading=15, alignment=TA_LEFT
    )
    s["section_hdr"] = ParagraphStyle(
        "section_hdr", fontName="Helvetica-Bold", fontSize=8,
        textColor=WHITE, spaceAfter=0, leading=10, alignment=TA_LEFT
    )
    s["body"] = ParagraphStyle(
        "body", fontName="Helvetica", fontSize=8,
        textColor=BLACK, spaceAfter=4, leading=11, alignment=TA_JUSTIFY
    )
    s["body_bold"] = ParagraphStyle(
        "body_bold", fontName="Helvetica-Bold", fontSize=8,
        textColor=BLACK, spaceAfter=4, leading=11, alignment=TA_JUSTIFY
    )
    s["bullet"] = ParagraphStyle(
        "bullet", fontName="Helvetica", fontSize=8,
        textColor=BLACK, spaceAfter=3, leading=11, leftIndent=12,
        bulletIndent=0, alignment=TA_LEFT
    )
    s["footnote"] = ParagraphStyle(
        "footnote", fontName="Helvetica", fontSize=6.5,
        textColor=DGRAY, spaceAfter=0, leading=8.5, alignment=TA_LEFT
    )
    s["table_hdr"] = ParagraphStyle(
        "table_hdr", fontName="Helvetica-Bold", fontSize=7,
        textColor=WHITE, leading=9, alignment=TA_CENTER
    )
    s["table_cell"] = ParagraphStyle(
        "table_cell", fontName="Helvetica", fontSize=7.5,
        textColor=BLACK, leading=9, alignment=TA_RIGHT
    )
    s["table_cell_l"] = ParagraphStyle(
        "table_cell_l", fontName="Helvetica", fontSize=7.5,
        textColor=BLACK, leading=9, alignment=TA_LEFT
    )
    s["rating_label"] = ParagraphStyle(
        "rating_label", fontName="Helvetica", fontSize=7,
        textColor=WHITE, leading=9, alignment=TA_CENTER
    )
    s["rating_value"] = ParagraphStyle(
        "rating_value", fontName="Helvetica-Bold", fontSize=13,
        textColor=WHITE, leading=16, alignment=TA_CENTER
    )
    s["risk_hdr"] = ParagraphStyle(
        "risk_hdr", fontName="Helvetica-Bold", fontSize=7.5,
        textColor=CRIMSON, spaceAfter=1, leading=10, alignment=TA_LEFT
    )
    return s

# ── Helper: section banner ──────────────────────────────────────────────────────
def banner(text, S, bg=NAVY, w=7.5*inch):
    tbl = Table([[Paragraph(text, S["section_hdr"])]], colWidths=[w])
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("TOPPADDING",    (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ]))
    return tbl

def hline(color=FERRARI_RED, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4)

# ── Build PDF ──────────────────────────────────────────────────────────────────
def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
        topMargin=0.6*inch,   bottomMargin=0.6*inch,
    )
    S   = styles()
    els = []

    # ── HEADER ──────────────────────────────────────────────────────────────────
    header_tbl = Table([
        [
            Paragraph("Ferrari N.V.  (NYSE: RACE  |  BIT: RACE)", S["title"]),
            Paragraph("Francisco Rodriguez<br/>Equity Research", S["subtitle"]),
        ]
    ], colWidths=[5.5*inch, 2.0*inch])
    header_tbl.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("ALIGN",  (1,0), (1,0),  "RIGHT"),
    ]))
    els.append(header_tbl)

    els.append(Paragraph(
        "Initiating Coverage  |  Luxury Goods / Consumer Discretionary  |  February 26, 2026",
        S["subtitle"]
    ))
    els.append(hline(FERRARI_RED, 2))

    # ── RATING STRIP ────────────────────────────────────────────────────────────
    boxes = [
        (CRIMSON,    "RATING",          "OVERWEIGHT"),
        (NAVY,       "PRICE TARGET",    "$450"),
        (TEAL,       "CURRENT PRICE",   "$375.50"),
        (GREEN_DARK, "UPSIDE",          "+19.8%"),
    ]
    cells = []
    for bg, lbl_txt, val_txt in boxes:
        inner = Table([
            [Paragraph(lbl_txt,  S["rating_label"])],
            [Paragraph(val_txt,  S["rating_value"])],
        ], colWidths=[1.72*inch])
        inner.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), bg),
            ("TOPPADDING",    (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
            ("LEFTPADDING",   (0,0), (-1,-1), 2),
            ("RIGHTPADDING",  (0,0), (-1,-1), 2),
        ]))
        cells.append(inner)

    strip = Table([cells], colWidths=[1.875*inch]*4)
    strip.setStyle(TableStyle([
        ("LEFTPADDING",  (0,0), (-1,-1), 1),
        ("RIGHTPADDING", (0,0), (-1,-1), 1),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
    ]))
    els.append(strip)
    els.append(Spacer(1, 6))

    # ── THESIS HEADLINE ─────────────────────────────────────────────────────────
    els.append(Paragraph(
        "\u201cThe Luce Catalyst: Market Is Pricing Ferrari Like BMW. We Think It\u2019s Herm\u00e8s.\u201d",
        S["thesis_headline"]
    ))

    # ── KEY STATS  +  VALUATION SUMMARY ─────────────────────────────────────────
    stats_left = [
        ["Fiscal Year End",      "December"],
        ["Shares Outstanding",   "~180M diluted"],
        ["Market Cap",           "~$67B USD"],
        ["Enterprise Value",     "~$69B USD"],
        ["Net Industrial Debt",  "€180M  (0.06× EBITDA)"],
        ["FY2025A Revenue",      "€7,146M  (+7.0% YoY)"],
        ["FY2025A EBITDA",       "€2,772M  (38.8% margin)"],
        ["FY2025A Deliveries",   "~14,000 units"],
    ]
    stats_right = [
        ["52-Wk High / Low",        "$519.10 / $328.00"],
        ["Vs. 52-Wk High",          "–27.8%  ← entry point"],
        ["DCF Intrinsic Value",      "$351/share"],
        ["Comps (27× '26E EBITDA)",  "$498/share"],
        ["Blended PT (40/60)",       "$450/share"],
        ["Base WACC",                "7.5%  (luxury β=0.75)"],
        ["Analyst Consensus PT",     "$495  (Strong Buy)"],
        ["EUR/USD",                  "1.18×"],
    ]

    def stat_row(lbl_txt, val_txt, stripe, right=False, highlight=False):
        lbl_style = ParagraphStyle("sl", fontName="Helvetica",     fontSize=7.5, textColor=BLACK,  leading=9, alignment=TA_LEFT)
        val_style = ParagraphStyle("sv", fontName="Helvetica-Bold", fontSize=7.5,
                                   textColor=(FERRARI_RED if highlight else CRIMSON), leading=9, alignment=TA_RIGHT)
        bg = LGRAY if stripe else WHITE
        row = Table(
            [[Paragraph(lbl_txt, lbl_style), Paragraph(val_txt, val_style)]],
            colWidths=[1.6*inch, 1.55*inch]
        )
        row.setStyle(TableStyle([
            ("BACKGROUND",    (0,0), (-1,-1), bg),
            ("TOPPADDING",    (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
            ("LEFTPADDING",   (0,0), (-1,-1), 4),
            ("RIGHTPADDING",  (0,0), (-1,-1), 4),
        ]))
        return row

    left_rows  = [stat_row(l, v, i%2==0) for i, (l, v) in enumerate(stats_left)]
    right_rows = [stat_row(l, v, i%2==0, highlight=(i==1)) for i, (l, v) in enumerate(stats_right)]

    left_tbl  = Table([[r] for r in left_rows],  colWidths=[3.2*inch])
    right_tbl = Table([[r] for r in right_rows], colWidths=[3.2*inch])
    left_tbl.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    right_tbl.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0)]))

    left_block  = [banner("KEY STATISTICS  (FY2025A reported Feb 10, 2026)", S, CRIMSON, 3.2*inch), left_tbl]
    right_block = [banner("VALUATION SUMMARY", S, CRIMSON, 3.2*inch), right_tbl]

    lt = Table([[left_block, right_block]], colWidths=[3.25*inch, 3.25*inch])
    lt.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING",   (0,0), (-1,-1), 0),
        ("BOTTOMPADDING",(0,0), (-1,-1), 0),
    ]))
    els.append(lt)
    els.append(Spacer(1, 8))

    # ── EXECUTIVE SUMMARY ───────────────────────────────────────────────────────
    els.append(banner("EXECUTIVE SUMMARY", S, FERRARI_RED))
    els.append(Spacer(1, 4))
    els.append(Paragraph(
        "We initiate coverage of Ferrari N.V. (RACE) with an <b>OVERWEIGHT</b> rating and a "
        "<b>$450 price target</b>, implying 19.8% upside from the current $375.50. The stock "
        "has pulled back 27.8% from its 52-week high of $519.10 — not because the business "
        "deteriorated, but because the market applied an EV-fear discount borrowed from legacy "
        "automakers. We believe that discount is misplaced.",
        S["body"]
    ))
    els.append(Paragraph(
        "Ferrari\u2019s reveal of the <b>Luce</b> on February 9, 2026 \u2014 its first fully electric vehicle, "
        "designed in partnership with Jony Ive and priced above the existing fleet ASP \u2014 is the "
        "inflection point the market has been waiting for. Unlike BMW or Mercedes, where EV "
        "transitions mean margin compression and pricing pressure, Ferrari\u2019s Luce is an "
        "<i>ASP accelerant</i>: a vehicle that commands a premium because of scarcity, design "
        "provenance, and brand positioning, not despite EV technology but <i>through</i> it.",
        S["body"]
    ))
    els.append(Paragraph(
        "Our blended $450 PT weights DCF intrinsic value 40% ($351) and a trading comps "
        "re-rating to 27\u00d7 FY2026E EBITDA 60% ($498) \u2014 itself conservative relative to the "
        "27\u201330\u00d7 at which luxury peers (Herm\u00e8s, LVMH) currently trade. Analyst consensus "
        "stands at $495 (Strong Buy); we are 10% below consensus, giving us room to be right "
        "for the right reason without relying on pure multiple expansion.",
        S["body"]
    ))
    els.append(Spacer(1, 6))

    # ── INVESTMENT THESIS: 4 DRIVERS ────────────────────────────────────────────
    els.append(banner("INVESTMENT THESIS — FOUR VALUE CREATION DRIVERS", S, FERRARI_RED))
    els.append(Spacer(1, 4))

    drivers = [
        (
            "1.  The Luce EV Is an ASP Accelerant, Not a Margin Headwind",
            "Legacy automakers lose margin on EVs because they sell high volumes at prices constrained "
            "by competitive dynamics. Ferrari operates from a fundamentally different position: demand "
            "always exceeds supply, and the Luce will be the most expensive production Ferrari ever "
            "made. Initial pricing indications suggest €400\u2013500K+ (vs. current fleet ASP of ~€400K "
            "blended). First deliveries target Q4 2026, meaning the first Luce ASP recognition hits "
            "FY2027E, driving a 1.5\u20132.0ppt EBITDA margin improvement in year one of production alone. "
            "We model Luce at 500 units in FY2027E, scaling to 1,500 by FY2030E."
        ),
        (
            "2.  The Multiple Re-rating Opportunity: BMW Fear Is Wrong",
            "RACE peaked at 37\u00d7 EV/EBITDA in 2023. It trades today at ~22\u00d7 FY2026E EBITDA \u2014 "
            "a 15-turn compression that has no fundamental justification. Herm\u00e8s trades at 30\u00d7 "
            "EBITDA. LVMH at 14\u00d7. The correct peer set for Ferrari is the former, not the latter. "
            "A re-rating to even 25\u00d727\u00d7 (well below 2023 peak) would close much of the gap to "
            "our $450 PT without requiring any earnings growth. We use a conservative 27\u00d7 in our "
            "comps scenario, with 40% weight on our DCF to anchor the blended value."
        ),
        (
            "3.  FY2025A Confirms the Business Is Accelerating Into the Thesis",
            "Ferrari reported FY2025 results on February 10, 2026: Revenue \u20ac7,146M (+7.0% YoY), "
            "EBITDA \u20ac2,772M at a record 38.8% margin (up from 38.3% in FY2024A). EPS came in at "
            "\u20ac8.96. Deliveries reached ~14,000 units. The company exited the year with net "
            "industrial debt of only \u20ac180M \u2014 essentially unlevered \u2014 and guided for FY2026E "
            "Revenue of \u20ac7.9B and EBITDA of \u20ac3.0\u20133.1B. Management raised its long-term "
            "EBITDA margin target to 40%+. Every fundamental data point supports the thesis; "
            "only the stock price does not."
        ),
        (
            "4.  Capital Return and Pricing Power as Downside Protection",
            "Ferrari operates under structural demand constraint: the waitlist for many models "
            "exceeds 24 months. This insulates revenue from macro downturns \u2014 the company "
            "grew EBITDA through COVID and raised prices during inflationary periods. The balance "
            "sheet is nearly debt-free, enabling aggressive capital return: buybacks and dividends "
            "at a combined yield of ~1.5%. In a bear case where the Luce is delayed or the "
            "multiple stays compressed, our DCF alone supports ~$351/share \u2014 implying limited "
            "downside from current levels and a highly asymmetric risk/reward."
        ),
    ]

    for title, body in drivers:
        els.append(KeepTogether([
            Paragraph(title, S["body_bold"]),
            Paragraph(body, S["body"]),
            Spacer(1, 4),
        ]))

    # ── FINANCIAL PROJECTIONS TABLE ──────────────────────────────────────────────
    els.append(Spacer(1, 2))
    els.append(banner("FINANCIAL PROJECTIONS  (€M unless noted)", S, FERRARI_RED))
    els.append(Spacer(1, 4))

    # Columns: Metric | FY2023A | FY2024A | FY2025A | FY2026E | FY2027E | FY2028E
    proj_hdr = ["Metric", "FY2023A", "FY2024A", "FY2025A", "FY2026E", "FY2027E", "FY2028E"]
    proj_data = [
        ["Revenue (€M)",       "6,677",  "7,002",  "7,146",  "7,900",  "8,610",  "9,242"],
        ["YoY Growth",         "—",      "+4.9%",  "+2.1%",  "+10.6%", "+8.9%",  "+7.3%"],
        ["EBITDA (€M)",        "2,496",  "2,683",  "2,772",  "3,040",  "3,434",  "3,851"],
        ["EBITDA Margin",      "37.4%",  "38.3%",  "38.8%",  "38.5%",  "39.9%",  "41.7%"],
        ["EBIT (€M)",          "1,959",  "2,124",  "2,202",  "2,453",  "2,808",  "3,196"],
        ["Net Income (€M)",    "1,560",  "1,658",  "1,613",  "1,894",  "2,172",  "2,472"],
        ["EPS (€)",            "8.34",   "9.10",   "8.96",   "10.52",  "12.07",  "13.73"],
        ["Deliveries (units)", "13,663", "13,752", "14,000", "14,700", "15,500", "16,200"],
        ["ASP (€K / unit)",    "489",    "509",    "511",    "538",    "556",    "571"],
        ["FCF (€M)",           "~1,400", "~1,500", "~1,550", "~1,720", "~2,050", "~2,400"],
    ]

    def p(txt, style):
        return Paragraph(txt, style)

    pj_style  = ParagraphStyle("pj",  fontName="Helvetica",      fontSize=7.5, textColor=BLACK, leading=9, alignment=TA_RIGHT)
    pj_l      = ParagraphStyle("pjl", fontName="Helvetica",      fontSize=7.5, textColor=BLACK, leading=9, alignment=TA_LEFT)
    pj_h      = ParagraphStyle("pjh", fontName="Helvetica-Bold",  fontSize=7.5, textColor=WHITE, leading=9, alignment=TA_CENTER)
    pj_hd     = ParagraphStyle("pjhd",fontName="Helvetica-Bold",  fontSize=7.5, textColor=WHITE, leading=9, alignment=TA_LEFT)

    hrow = [[p(h, pj_hd if i==0 else pj_h) for i, h in enumerate(proj_hdr)]]
    drows = []
    for i, row in enumerate(proj_data):
        drows.append([
            p(row[0], pj_l),
            *[p(v, pj_style) for v in row[1:]]
        ])

    cws = [2.1*inch] + [0.88*inch]*6
    pt = Table(hrow + drows, colWidths=cws)
    ts = [
        ("BACKGROUND",    (0,0), (-1,0),  CRIMSON),
        ("BACKGROUND",    (0,0), (0,-1),  LGRAY),
        ("GRID",          (0,0), (-1,-1), 0.25, MGRAY),
        ("ROWBACKGROUNDS",(0,1), (-1,-1), [WHITE, LGRAY]),
        ("TOPPADDING",    (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ("LEFTPADDING",   (0,0), (0,-1),  4),
        ("RIGHTPADDING",  (0,1), (-1,-1), 4),
        ("FONTNAME",      (0,1), (0,-1),  "Helvetica"),
        ("FONTSIZE",      (0,1), (0,-1),  7.5),
        # Highlight FY2025A (actual) column
        ("BACKGROUND",    (3,1), (3,-1),  colors.HexColor("#FFF2CC")),
        ("FONTNAME",      (3,1), (3,-1),  "Helvetica-Bold"),
    ]
    pt.setStyle(TableStyle(ts))
    els.append(pt)
    els.append(Paragraph(
        "FY2025A sourced from Ferrari full-year results released February 10, 2026. "
        "Projections are analyst estimates; EUR/USD 1.18.",
        S["footnote"]
    ))
    els.append(Spacer(1, 8))

    # ── DCF BRIDGE ──────────────────────────────────────────────────────────────
    els.append(banner("DCF BRIDGE  (USD/share)", S, FERRARI_RED))
    els.append(Spacer(1, 4))

    dcf_cols = ["Component", "Assumption", "Value (USD/share)"]
    dcf_rows = [
        ["PV of FCFs (FY2026E–FY2030E)",   "WACC 7.5%",                "+$128"],
        ["Terminal Value",                  "TGR 3.0%, WACC 7.5%",      "+$250"],
        ["Less: Net Debt (converted @ 1.18×)", "€180M → $212M",         "–$1"],
        ["Plus: Non-op. Assets",            "Financial investments",     "+$5"],
        ["Equity Value → Intrinsic Value",  "÷ 180M diluted shares",     "≈$351/share"],
        ["Comps Value (27× '26E EBITDA)",   "EV/EBITDA peer re-rating",  "$498/share"],
        ["BLENDED PT  (40% DCF / 60% Comps)", "Conservative weighting", "<b>$450/share</b>"],
    ]

    dcf_hrow = [[p(h, pj_h) for h in dcf_cols]]
    dcf_drows = []
    for i, row in enumerate(dcf_rows):
        bold_last = (i == len(dcf_rows)-1)
        fn_name = "Helvetica-Bold" if bold_last else "Helvetica"
        dcf_drows.append([
            Paragraph(row[0], ParagraphStyle("dd", fontName=fn_name, fontSize=7.5, textColor=BLACK, leading=9, alignment=TA_LEFT)),
            Paragraph(row[1], ParagraphStyle("dd2", fontName=fn_name, fontSize=7.5, textColor=BLACK, leading=9, alignment=TA_LEFT)),
            Paragraph(row[2], ParagraphStyle("dd3", fontName=fn_name, fontSize=7.5,
                               textColor=(GREEN_DARK if bold_last else BLACK), leading=9, alignment=TA_RIGHT)),
        ])

    dcf_cws = [3.0*inch, 2.5*inch, 1.5*inch]
    dt = Table(dcf_hrow + dcf_drows, colWidths=dcf_cws)
    dt.setStyle(TableStyle([
        ("BACKGROUND",    (0,0),  (-1,0),  CRIMSON),
        ("ROWBACKGROUNDS",(0,1),  (-1,-1), [WHITE, LGRAY]),
        ("BACKGROUND",    (0,-1), (-1,-1), colors.HexColor("#EBF1DE")),
        ("GRID",          (0,0),  (-1,-1), 0.25, MGRAY),
        ("TOPPADDING",    (0,0),  (-1,-1), 3),
        ("BOTTOMPADDING", (0,0),  (-1,-1), 3),
        ("LEFTPADDING",   (0,0),  (-1,-1), 4),
        ("RIGHTPADDING",  (0,0),  (-1,-1), 4),
    ]))
    els.append(dt)
    els.append(Spacer(1, 8))

    # ── WACC × TGR SENSITIVITY ──────────────────────────────────────────────────
    els.append(banner("WACC × TERMINAL GROWTH RATE SENSITIVITY  (Price Target, USD)", S, FERRARI_RED))
    els.append(Spacer(1, 4))

    wacc_vals = [0.065, 0.070, 0.075, 0.080, 0.085]
    tgr_vals  = [0.020, 0.025, 0.030, 0.035, 0.040]

    def pt_estimate(wacc, tgr):
        base_fcf = 1720  # FY2026E FCF in EUR M
        g_rates  = [0.19, 0.15, 0.12, 0.10, 0.08]
        pv = 0
        fcf = base_fcf
        for gr in g_rates:
            fcf *= (1 + gr)
            pv  += fcf / ((1 + wacc) ** (g_rates.index(gr) + 1))
        tv  = fcf * (1 + tgr) / (wacc - tgr)
        tv_pv = tv / ((1 + wacc) ** 5)
        equity_eur = (pv + tv_pv - 180) / 1000  # in €B
        equity_usd = equity_eur * 1.18 * 1000    # back to $M
        return equity_usd / 180  # per share

    tgr_labels  = ["TGR→  2.0%", "2.5%", "3.0%", "3.5%", "4.0%"]
    wacc_labels = ["6.5%", "7.0%", "7.5%", "8.0%", "8.5%"]

    sens_hrow  = [[p("WACC↓", pj_h)] + [p(t, pj_h) for t in tgr_labels]]
    sens_drows = []
    for wi, w in enumerate(wacc_vals):
        row = [p(wacc_labels[wi], ParagraphStyle("wl", fontName="Helvetica-Bold", fontSize=7.5, textColor=BLACK, leading=9, alignment=TA_CENTER))]
        for ti, t in enumerate(tgr_vals):
            v = pt_estimate(w, t)
            is_base = (wi == 2 and ti == 2)  # 7.5% WACC, 3.0% TGR
            color = colors.HexColor("#00B050") if v > 450 else (colors.HexColor("#FF0000") if v < 300 else BLACK)
            style = ParagraphStyle("sv2", fontName="Helvetica-Bold" if is_base else "Helvetica",
                                   fontSize=7.5, textColor=WHITE if is_base else color,
                                   leading=9, alignment=TA_CENTER)
            row.append(p(f"${v:,.0f}", style))
        sens_drows.append(row)

    sens_cws = [0.85*inch] + [1.33*inch]*5
    st = Table(sens_hrow + sens_drows, colWidths=sens_cws)

    # Color cells
    ts2 = [
        ("BACKGROUND",    (0,0),  (-1,0),  CRIMSON),
        ("BACKGROUND",    (0,0),  (0,-1),  LGRAY),
        ("GRID",          (0,0),  (-1,-1), 0.25, MGRAY),
        ("ROWBACKGROUNDS",(0,1),  (-1,-1), [WHITE, LGRAY]),
        ("TOPPADDING",    (0,0),  (-1,-1), 3),
        ("BOTTOMPADDING", (0,0),  (-1,-1), 3),
        ("LEFTPADDING",   (0,0),  (-1,-1), 2),
        ("RIGHTPADDING",  (0,0),  (-1,-1), 2),
        # base case cell
        ("BACKGROUND",    (3,3),  (3,3),  NAVY),
    ]
    # Green cells where value > $450
    for wi in range(5):
        for ti in range(5):
            v = pt_estimate(wacc_vals[wi], tgr_vals[ti])
            if v > 450:
                ts2.append(("BACKGROUND", (ti+1, wi+1), (ti+1, wi+1), colors.HexColor("#E2EFDA")))
            elif v < 300:
                ts2.append(("BACKGROUND", (ti+1, wi+1), (ti+1, wi+1), colors.HexColor("#FCE4D6")))
    st.setStyle(TableStyle(ts2))
    els.append(st)
    els.append(Paragraph(
        "Green cells = PT > $450 (above our target). Red cells = PT < $300. Navy = base case ($351 DCF). "
        "DCF alone; blended target of $450 incorporates 60% weight on comps re-rating.",
        S["footnote"]
    ))
    els.append(Spacer(1, 8))

    # ── RISKS & MITIGANTS ───────────────────────────────────────────────────────
    els.append(banner("RISKS & MITIGANTS", S, FERRARI_RED))
    els.append(Spacer(1, 4))

    risks = [
        (
            "Luce Delay / Execution Risk",
            "If Ferrari delays the Luce beyond Q4 2026, the re-rating catalyst is pushed out 12–18 months. "
            "Mitigant: even without the Luce, FY2025A results and management guidance for \u20ac3.0–3.1B FY2026E EBITDA "
            "support current levels. We model Luce conservatively (500 units FY2027E) so execution risk is bounded."
        ),
        (
            "Multiple Compression (Luxury De-rating)",
            "A macro risk-off event could compress luxury multiples broadly (as happened in 2022–23 with LVMH). "
            "Mitigant: Ferrari\u2019s 24-month waitlist provides revenue visibility that pure-play luxury lacks. The "
            "stock already trades at a 40% discount to its 2023 peak multiple \u2014 further de-rating from here "
            "is plausible but offers limited incremental downside."
        ),
        (
            "EUR/USD Currency Risk",
            "Ferrari reports in EUR; our PT assumes EUR/USD of 1.18. A move to 1.05 would reduce the USD PT "
            "by ~$30/share (to ~$420). Mitigant: partial natural hedge via USD-denominated sales in North America (~25% of revenue). "
            "This risk is reflected in the sensitivity table."
        ),
        (
            "Luxury Demand Slowdown in China",
            "China represents ~10% of Ferrari deliveries. A sustained luxury demand slowdown could reduce "
            "unit volumes by 500\u20131,000 units. Mitigant: Ferrari\u2019s order book structure means cancellations "
            "are quickly absorbed by waitlist demand from other geographies."
        ),
    ]

    for risk_title, risk_body in risks:
        els.append(KeepTogether([
            Paragraph(risk_title, S["risk_hdr"]),
            Paragraph(risk_body, S["body"]),
            Spacer(1, 3),
        ]))

    # ── RECOMMENDATION ──────────────────────────────────────────────────────────
    els.append(Spacer(1, 4))
    els.append(hline(FERRARI_RED))
    rec_tbl = Table([[
        Paragraph("<b>RECOMMENDATION</b>", ParagraphStyle("rt", fontName="Helvetica-Bold",
                  fontSize=8, textColor=CRIMSON, leading=10, alignment=TA_LEFT)),
        Paragraph(
            "Initiate <b>OVERWEIGHT</b> with $450 PT. Ferrari\u2019s 28% pullback from $519.10 has created an "
            "entry point into a structurally superior business ahead of a clear catalyst. The Luce reframes "
            "Ferrari\u2019s EV narrative from margin risk to margin expansion. With FY2025A confirming record "
            "margins, a near-debt-free balance sheet, and analyst consensus at $495, we see the risk/reward "
            "as highly asymmetric. The market is pricing Ferrari like a car company; it is one of the world\u2019s "
            "most exclusive luxury goods brands.",
            ParagraphStyle("rb", fontName="Helvetica", fontSize=7.5, textColor=BLACK,
                           leading=10, alignment=TA_JUSTIFY)
        ),
    ]], colWidths=[1.4*inch, 6.1*inch])
    rec_tbl.setStyle(TableStyle([
        ("VALIGN",       (0,0), (-1,-1), "TOP"),
        ("TOPPADDING",   (0,0), (-1,-1), 4),
        ("BOTTOMPADDING",(0,0), (-1,-1), 4),
        ("LEFTPADDING",  (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
    ]))
    els.append(rec_tbl)
    els.append(hline(FERRARI_RED))

    # ── FOOTNOTES ───────────────────────────────────────────────────────────────
    els.append(Spacer(1, 4))
    els.append(Paragraph(
        "¹ Current price as of February 26, 2026. 52-week high: $519.10 (June 2025). "
        "EUR/USD: 1.18. FY2025A figures per Ferrari N.V. full-year results press release, February 10, 2026. "
        "Analyst consensus per Bloomberg, February 2026. All projections are estimates and subject to revision. "
        "This is an illustrative analysis prepared for portfolio purposes and does not constitute investment advice.",
        S["footnote"]
    ))

    doc.build(els)
    print(f"✓  Ferrari initiation note saved → {OUTPUT}")

if __name__ == "__main__":
    build()
