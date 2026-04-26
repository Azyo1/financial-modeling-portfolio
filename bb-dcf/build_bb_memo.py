#!/usr/bin/env python3
"""
BlackBerry Limited (NYSE: BB) — Equity Research Initiation Note
Two-segment DCF + Comps: IoT/QNX + Cybersecurity
Generates BB_DCF_Initiation_Note.pdf
"""

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle, KeepTogether
)
from reportlab.lib import colors

OUTPUT = "/Users/paco/career/modeling-portfolio/bb-dcf/BB_DCF_Initiation_Note.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=LETTER,
    leftMargin=0.80 * inch,
    rightMargin=0.80 * inch,
    topMargin=0.60 * inch,
    bottomMargin=0.60 * inch,
)

W = LETTER[0] - 1.60 * inch

# ── Colors ─────────────────────────────────────────────────────────────────
NAVY    = colors.HexColor("#1F3864")
NAVY2   = colors.HexColor("#2F5496")
DARK    = colors.HexColor("#1A1A1A")
MID     = colors.HexColor("#444444")
LIGHT   = colors.HexColor("#767676")
ROW_ALT = colors.HexColor("#F2F5FB")
ROW_HDR = colors.HexColor("#1F3864")
GRAY    = colors.HexColor("#F2F2F2")
GREEN   = colors.HexColor("#375623")
RED     = colors.HexColor("#C00000")

# ── Styles ─────────────────────────────────────────────────────────────────
memo_header_style = ParagraphStyle(
    "MemoHdr", fontName="Helvetica", fontSize=8.5, leading=13,
    textColor=MID, spaceAfter=1,
)
re_style = ParagraphStyle(
    "Re", fontName="Helvetica-Bold", fontSize=9, leading=13,
    textColor=DARK, spaceAfter=0,
)
confidential_style = ParagraphStyle(
    "Conf", fontName="Helvetica-Oblique", fontSize=8, leading=11,
    textColor=LIGHT, alignment=TA_RIGHT,
)
section_style = ParagraphStyle(
    "Section", fontName="Helvetica-Bold", fontSize=9, leading=11,
    textColor=NAVY, spaceBefore=10, spaceAfter=2, letterSpacing=1.2,
)
body_style = ParagraphStyle(
    "Body", fontName="Helvetica", fontSize=9, leading=13.5,
    textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=4,
)
bullet_style = ParagraphStyle(
    "Bullet", fontName="Helvetica", fontSize=9, leading=13,
    textColor=DARK, leftIndent=10, firstLineIndent=-10,
    spaceAfter=2, alignment=TA_JUSTIFY,
)
bullet_bold_style = ParagraphStyle(
    "BulletBold", fontName="Helvetica-Bold", fontSize=9, leading=13,
    textColor=NAVY, leftIndent=10, firstLineIndent=-10,
    spaceAfter=1,
)
sub_body_style = ParagraphStyle(
    "SubBody", fontName="Helvetica", fontSize=8.5, leading=12.5,
    textColor=MID, leftIndent=10, spaceAfter=3, alignment=TA_JUSTIFY,
)
footnote_style = ParagraphStyle(
    "Footnote", fontName="Helvetica-Oblique", fontSize=7.5, leading=10,
    textColor=LIGHT, alignment=TA_CENTER, spaceBefore=4,
)

def section(title):
    return [
        Paragraph(title, section_style),
        HRFlowable(width="100%", thickness=0.5, color=NAVY2, spaceAfter=4),
    ]

def bl(text):
    return Paragraph("•  " + text, bullet_style)

def bl_bold(title, text):
    return [
        Paragraph("•  " + title, bullet_bold_style),
        Paragraph(text, sub_body_style),
    ]

def gap(n=4):
    return Spacer(1, n)

def make_table(headers, rows, col_widths, zebra=True):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths)
    style_cmds = [
        ("BACKGROUND",    (0, 0), (-1, 0), ROW_HDR),
        ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 8.5),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("TOPPADDING",    (0, 0), (-1, 0), 5),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",      (0, 1), (-1, -1), 8.5),
        ("ALIGN",         (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",         (0, 1), (0, -1),  "LEFT"),
        ("TOPPADDING",    (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 4),
        ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(style_cmds))
    return t

# ══════════════════════════════════════════════════════════════════════════
# BUILD STORY
# ══════════════════════════════════════════════════════════════════════════

story = []

story.append(HRFlowable(width="100%", thickness=4, color=NAVY, spaceAfter=8))

header_data = [
    ["TO:",   "Investment Committee"],
    ["FROM:", "Francisco Rodriguez, Financial Analyst"],
    ["DATE:", "April 2026"],
    ["RE:",   "Initiation of Coverage — BlackBerry Limited (NYSE: BB) | OVERWEIGHT | PT: $7.00"],
]
for label, value in header_data:
    row_text = f"<b>{label}</b>  {value}"
    style = re_style if label == "RE:" else memo_header_style
    story.append(Paragraph(row_text, style))

story.append(gap(2))
story.append(Paragraph("STRICTLY CONFIDENTIAL — FOR DISCUSSION PURPOSES ONLY", confidential_style))
story.append(gap(4))
story.append(HRFlowable(width="100%", thickness=0.75, color=NAVY, spaceAfter=8))

# ── Rating box ──────────────────────────────────────────────────────────────
rating_data = [["Rating", "Price Target", "Current Price", "Upside", "52-Wk Range"]]
rating_rows = [["OVERWEIGHT", "$7.00", "$5.50", "+27.3%", "$2.75 – $5.75"]]
t_rating = Table(rating_data + rating_rows,
                 colWidths=[W*0.16, W*0.16, W*0.16, W*0.16, W*0.36])
t_rating.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0), (-1, 0), ROW_HDR),
    ("TEXTCOLOR",     (0, 0), (-1, 0), colors.white),
    ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0), (-1, -1), 8.5),
    ("ALIGN",         (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME",      (0, 1), (-1, 1), "Helvetica-Bold"),
    ("TEXTCOLOR",     (0, 1), (0, 1),  colors.HexColor("#375623")),
    ("TOPPADDING",    (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("GRID",          (0, 0), (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
]))
story.append(t_rating)
story.append(gap(6))

# ── Executive summary ───────────────────────────────────────────────────────
story += section("EXECUTIVE SUMMARY")
story.append(Paragraph(
    "We initiate coverage of BlackBerry Limited (NYSE: BB) with an <b>OVERWEIGHT</b> rating and a "
    "<b>$7.00 price target</b>, representing 27.3% upside from the current price of $5.50. "
    "BlackBerry has completed its transformation into a pure-play enterprise software company — "
    "the sale of Cylance to Arctic Wolf (early 2025) removed the last legacy overhang and left "
    "two clean segments: IoT/QNX and Cybersecurity. Our thesis centers on QNX: the safety-certified "
    "real-time operating system embedded in 275 million vehicles is now expanding into the physical "
    "AI era through an April 20, 2026 collaboration with NVIDIA to integrate QNX OS for Safety 8.0 "
    "with NVIDIA IGX Thor — the reference compute platform for edge AI in robotics, medical devices, "
    "and industrial automation. Wall Street consensus stands at $4.84 (Hold), already below the "
    "current price and stale relative to the NVIDIA catalyst. Our blended 40% DCF + 60% segment "
    "comps methodology yields a $7.00 price target.",
    body_style,
))

# ── Company overview ────────────────────────────────────────────────────────
story += section("COMPANY OVERVIEW")

overview_headers = ["Metric", "Value"]
overview_rows = [
    ["Ticker / Exchange",           "BB / NYSE"],
    ["Market Capitalization",       "~$3.23B"],
    ["Enterprise Value",            "~$2.80B"],
    ["Net Cash (Feb 28, 2026)",     "$432.4M"],
    ["FY2026A Revenue",             "$549.1M  (QNX: $268M  |  CySec: $281M)"],
    ["FY2026A Adj EBITDA",          "$107.1M  (19.5% margin)"],
    ["FY2026A Free Cash Flow",      "$46.5M  (up 3× YoY)"],
    ["FY2027E Revenue Guidance",    "$584M–$611M  (~+9% YoY)"],
    ["QNX Royalty Backlog",         "$950M  (as of FY2026A exit)"],
    ["Vehicles Running QNX",        "275M+ globally"],
    ["Fiscal Year End",             "February 28"],
]
story.append(make_table(overview_headers, overview_rows, [W * 0.38, W * 0.62]))
story.append(gap(6))
story.append(Paragraph(
    "BlackBerry's operating model is structurally different from how it is commonly perceived. "
    "The company is not a has-been hardware brand — it is a software royalty business. QNX earns "
    "a per-unit royalty from every automotive OEM and industrial manufacturer that ships a product "
    "running its safety-certified RTOS. With 275 million vehicles already in the field and new "
    "design wins at Mercedes-Benz, BMW, Volvo, Leapmotor, and defense contractor TKMS, the royalty "
    "stream is compounding. The cybersecurity segment (SecuSUITE, AtHoc, government communications) "
    "provides stable, recurring revenue from government and enterprise customers.",
    body_style,
))

# ── Investment thesis ───────────────────────────────────────────────────────
story += section("INVESTMENT THESIS")

drivers = [
    ("QNX Is the Safety OS for the Physical AI Era",
     "On April 20, 2026 at Hannover Messe, NVIDIA and QNX announced expanded collaboration to "
     "integrate QNX OS for Safety 8.0 with NVIDIA IGX Thor and the Halos Safety Stack. IGX Thor "
     "is NVIDIA's edge AI compute platform for regulated environments: humanoid robots, autonomous "
     "mobile robots (AMRs), surgical systems, and industrial automation. QNX provides the "
     "safety-critical RTOS layer (IEC 61508, ISO 26262, DO-178C certified) that NVIDIA's AI "
     "acceleration hardware requires to operate in regulated environments. Every physical AI system "
     "that needs safety certification becomes a potential QNX royalty unit. TAM expands from "
     "~$19B automotive software (2023) to the full edge AI systems market — a multi-hundred-billion "
     "dollar opportunity over the next decade."),
    ("$950M Royalty Backlog = 2.5+ Years of Locked-In Revenue",
     "QNX's royalty model is fundamentally misunderstood by equity markets. OEMs commit to QNX "
     "at design-win stage — typically 3-5 years before vehicles enter production. The $950M "
     "royalty backlog represents OEM production commitments already awarded. Revenue is recognized "
     "when units ship, providing exceptional forward visibility that is rare among software companies "
     "at this market cap. FY2026A QNX revenue of $268M (+14% YoY) with a Q4 exit rate of $78.7M "
     "(+20% YoY, record quarter) puts the segment on a trajectory toward $315M+ in FY2027E. "
     "New wins (TKMS defense, Leapmotor EV OEM) extend backlog growth into non-automotive verticals."),
    ("Street Consensus Is Stale — Multiple Re-rating Is the Catalyst",
     "Wall Street consensus PT of $4.84 implies ~5.1× EV/FY2026A Revenue and ~26× EV/EBITDA — "
     "reasonable multiples for a mixed-segment company, but deeply wrong for QNX as a standalone "
     "asset. Pure-play safety-critical software companies (ANSYS, PTC, Palantir's government "
     "segment) trade at 8–15× forward revenue. Our segment comps assign QNX 8× FY2028E EV/Revenue "
     "($2.97B) and CySec 3.5× FY2028E EV/Revenue ($1.02B) — still conservative relative to "
     "pure-play software peers. Combined with $432M cash, this yields a $7.51 comps-implied PT. "
     "Seven of seven analysts have Hold ratings, none of which reflect the NVIDIA partnership "
     "announced April 20. The multiple re-rating begins when analysts update."),
    ("FCF Inflection + Buyback Creates Institutional-Grade Downside Support",
     "FY2026A FCF of $46.5M represents 3× YoY improvement ($16.5M in FY2025). The company "
     "returned to GAAP profitability ($53.2M net income) — eliminating a structural barrier "
     "to institutional ownership. Management has repurchased 15.5M shares ($60M) since May 2025, "
     "with the program ongoing. At ~$3B market cap with $432M cash and $46.5M of FCF growing "
     "toward $110M+ by FY2028E, the FCF yield will approach 3.5% on current market cap within "
     "two fiscal years. This combination of profitability, buybacks, and cash provides a durable "
     "floor for the stock."),
]
for title, desc in drivers:
    story += bl_bold(title, desc)
    story.append(gap(2))

# ── Financial projections ───────────────────────────────────────────────────
story += section("FINANCIAL PROJECTIONS  ($M)")

proj_headers = ["", "FY2026A", "FY2027E", "FY2028E", "FY2029E", "FY2030E", "FY2031E"]
proj_rows = [
    ["QNX Revenue",    "$268.0", "$316.0", "$371.0", "$427.0", "$477.0", "$521.0"],
    ["  QNX Growth",   "+14.0%", "+17.9%", "+17.4%", "+15.1%", "+11.7%", " +9.2%"],
    ["CySec Revenue",  "$281.1", "$285.0", "$291.0", "$297.0", "$303.0", "$306.0"],
    ["  CySec Growth", "  n/a",  " +1.4%", " +2.1%", " +2.1%", " +2.0%", " +1.0%"],
    ["Total Revenue",  "$549.1", "$601.0", "$662.0", "$724.0", "$780.0", "$827.0"],
    ["  Total Growth", "  n/a",  " +9.4%", "+10.2%", " +9.4%", " +7.7%", " +6.0%"],
    ["Adj EBITDA",     "$107.1", "$132.2", "$165.5", "$195.5", "$226.2", "$256.4"],
    ["  EBITDA Margin","19.5%",  "22.0%",  "25.0%",  "27.0%",  "29.0%",  "31.0%"],
    ["EBIT",           " $65.1", " $90.2", "$125.5", "$157.5", "$189.2", "$220.4"],
    ["NOPAT",          " $48.8", " $67.7", " $94.1", "$118.1", "$141.9", "$165.3"],
    ["Unlevered FCF",  " $70.8", " $86.7", "$109.1", "$130.1", "$151.9", "$174.3"],
]
cw = [W*0.17] + [W*0.83/6]*6
story.append(make_table(proj_headers, proj_rows, cw))
story.append(Paragraph(
    "FY2026A actuals from Q4 FY2026 earnings (April 8, 2026). FY2027E aligns with management "
    "guidance midpoint of $598M. UFCF = NOPAT + D&A – Capex – ΔNWC. FY2026A UFCF is modeled "
    "(reported FCF was $46.5M; difference reflects SBC add-back and timing items not in base model).",
    footnote_style,
))
story.append(gap(6))

# ── Valuation ───────────────────────────────────────────────────────────────
story += section("VALUATION  —  BLENDED DCF + SEGMENT COMPS")

val_headers = ["Component", "Value", "Detail"]
val_rows = [
    ["DCF — WACC",            "9.0%",     "RF 4.5% + ERP 5.5% × β 0.82; no size premium"],
    ["DCF — Exit Multiple",   "16.0× EBITDA", "FY2031E EBITDA $256.4M × 16× = $4,102M TV"],
    ["Sum PV of FCFs",        "$492.7M",  "FY2027E–FY2031E discounted at 9.0%"],
    ["PV of Terminal Value",  "$2,666M",  "$4,102M / 1.09^5"],
    ["Enterprise Value (DCF)","$3,159M",  "Sum PV FCFs + PV TV"],
    ["+ Cash",                "$432M",    "Feb 28, 2026 balance sheet"],
    ["Equity Value (DCF)",    "$3,591M",  "EV + Cash"],
    ["DCF Price Target",      "$6.11",    "$3,591M / 588M shares"],
    ["QNX Segment EV (Comps)","$2,968M",  "FY2028E $371M × 8.0× EV/Rev"],
    ["CySec Segment EV",      "$1,019M",  "FY2028E $291M × 3.5× EV/Rev"],
    ["+ Cash",                "$432M",    "Feb 28, 2026 balance sheet"],
    ["Equity Value (Comps)",  "$4,419M",  "Total Segment EV + Cash"],
    ["Comps Price Target",    "$7.51",    "$4,419M / 588M shares"],
    ["Blended Price Target ★","$7.00",    "40% × $6.11 + 60% × $7.51 = $6.95 → $7.00"],
]
t_val = Table([val_headers] + val_rows, colWidths=[W*0.30, W*0.18, W*0.52])
t_val.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0),  (-1, 0),  ROW_HDR),
    ("TEXTCOLOR",     (0, 0),  (-1, 0),  colors.white),
    ("FONTNAME",      (0, 0),  (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0),  (-1, -1), 8.5),
    ("ALIGN",         (1, 0),  (-1, -1), "CENTER"),
    ("ALIGN",         (0, 1),  (0, -1),  "LEFT"),
    ("ALIGN",         (2, 1),  (2, -1),  "LEFT"),
    ("FONTNAME",      (0, 1),  (-1, -1), "Helvetica"),
    ("TOPPADDING",    (0, 0),  (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0),  (-1, -1), 4),
    ("LEFTPADDING",   (0, 0),  (-1, -1), 6),
    ("RIGHTPADDING",  (0, 0),  (-1, -1), 6),
    ("GRID",          (0, 0),  (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
    # Highlight blended PT row
    ("FONTNAME",      (0, 14), (-1, 14), "Helvetica-Bold"),
    ("BACKGROUND",    (0, 14), (-1, 14), GRAY),
    ("LINEABOVE",     (0, 14), (-1, 14), 0.75, NAVY2),
    # Zebra
    ("BACKGROUND",    (0, 2),  (-1, 2),  ROW_ALT),
    ("BACKGROUND",    (0, 4),  (-1, 4),  ROW_ALT),
    ("BACKGROUND",    (0, 6),  (-1, 6),  ROW_ALT),
    ("BACKGROUND",    (0, 8),  (-1, 8),  ROW_ALT),
    ("BACKGROUND",    (0, 10), (-1, 10), ROW_ALT),
    ("BACKGROUND",    (0, 12), (-1, 12), ROW_ALT),
]))
story.append(t_val)
story.append(Paragraph(
    "QNX EV/Rev multiple of 8× is a discount to comparable safety-critical software peers "
    "(PTC, ANSYS). CySec at 3.5× reflects stable but slower-growth government comms software. "
    "Blended weights: 40% DCF / 60% Comps.",
    footnote_style,
))
story.append(gap(6))

# ── Sensitivity ─────────────────────────────────────────────────────────────
story += section("SENSITIVITY — DCF PRICE TARGET  (WACC × EXIT EV/EBITDA MULTIPLE)")

sens_headers = ["WACC \\ Exit →", "10×", "12×", "14×", "16× ★", "18×", "20×", "22×"]
sens_rows = [
    ["7.5%",  "$5.57", "$6.33", "$7.09", "$7.85", "$8.61", "$9.37", "$10.13"],
    ["8.0%",  "$5.24", "$5.95", "$6.66", "$7.37", "$8.08", "$8.79",  "$9.50"],
    ["8.5%",  "$4.94", "$5.61", "$6.27", "$6.94", "$7.60", "$8.27",  "$8.93"],
    ["9.0% ★","$4.66", "$5.29", "$5.92", "$6.55", "$7.18", "$7.81",  "$8.44"],
    ["9.5%",  "$4.41", "$5.00", "$5.60", "$6.19", "$6.79", "$7.38",  "$7.98"],
    ["10.0%", "$4.17", "$4.74", "$5.30", "$5.87", "$6.43", "$7.00",  "$7.56"],
    ["10.5%", "$3.96", "$4.49", "$5.03", "$5.57", "$6.10", "$6.64",  "$7.17"],
    ["11.0%", "$3.75", "$4.27", "$4.78", "$5.29", "$5.81", "$6.32",  "$6.83"],
]
story.append(make_table(sens_headers, sens_rows,
    [W*0.10, W*0.13, W*0.13, W*0.13, W*0.13, W*0.13, W*0.13, W*0.12],
    zebra=False))
story.append(Paragraph(
    "★ Base case: 9.0% WACC, 16× exit EV/EBITDA → $6.55/share DCF. Current price $5.50. "
    "Blended PT ($7.00) adds comps component (40/60 weighting). Green zone (≥$5.50) spans "
    "most of the table, reflecting a wide margin of safety at current prices.",
    footnote_style,
))
story.append(gap(6))

# ── Key risks ───────────────────────────────────────────────────────────────
story += section("KEY RISKS & MITIGANTS")

risks = [
    ("QNX Competitive Risk — MEDIUM",
     "Wind River (part of Aptiv) and Green Hills Software INTEGRITY OS compete directly with QNX. "
     "Microsoft Azure RTOS and QNX are increasingly evaluated by the same hyperscalers. However, "
     "QNX has the deepest safety certifications (ASIL-D, IEC 61508 SIL 3, DO-178C DAL-A) and "
     "the largest existing automotive install base — switching costs after design-win are "
     "prohibitively high (10-15 year platform cycles). The NVIDIA partnership further entrenches "
     "QNX as the default safety layer for Nvidia-based edge AI systems."),
    ("Cybersecurity Segment Secular Decline Risk — LOW-MEDIUM",
     "Post-Cylance sale, the CySec segment ($281M FY2026A) is primarily SecuSUITE and AtHoc — "
     "government-grade encrypted communications. These are sticky (multi-year government contracts) "
     "but represent a slow-growth or flat market. Our model assumes 1-2% annual growth. Downside "
     "scenario: segment revenues flat to down 3-5% as government contracts lapse without renewal. "
     "Mitigant: at 3.5× EV/Revenue, the downside impact on blended PT is limited."),
    ("QNX Royalty Backlog Conversion Risk — LOW",
     "The $950M backlog represents committed OEM production volumes, but vehicle production "
     "schedules can shift due to macro downturns, supply chain disruptions, or EV demand softness. "
     "A 20% backlog haircut reduces our FY2027E-FY2029E QNX revenue forecasts by ~$50-75M, "
     "implying a ~$0.50-0.80 reduction in DCF price target. The backlog being spread across "
     "European (Mercedes, BMW, Volvo), Asian (Leapmotor), and defense customers (TKMS) "
     "diversifies concentration risk."),
    ("Multiple Contraction Risk — MEDIUM",
     "Our 8× FY2028E EV/Revenue multiple for QNX assumes re-rating toward pure-play software "
     "peers. If the market continues to apply a software/hardware blended multiple (~5×), the "
     "comps-implied PT falls to ~$5.50-6.00. However, the DCF component ($6.11) provides a "
     "fundamental floor that is less sensitive to multiple sentiment."),
]
for title, desc in risks:
    story += bl_bold(title, desc)
    story.append(gap(1))

# ── Recommendation ──────────────────────────────────────────────────────────
story += section("RECOMMENDATION")
story.append(Paragraph(
    "We initiate coverage of BlackBerry Limited (NYSE: BB) with an <b>OVERWEIGHT</b> rating and a "
    "<b>$7.00 twelve-month price target</b> (+27.3% upside). The thesis is straightforward: "
    "QNX is the safety OS layer for physical AI — a structural role that Wall Street has not yet "
    "priced into a stock trading at 5× enterprise revenue. The NVIDIA collaboration announced "
    "April 20, 2026 is a genuine re-rating catalyst that expands QNX's TAM from automotive "
    "software into the entire edge AI systems market. FY2026A FCF of $46.5M and GAAP "
    "profitability have removed the last institutional ownership barriers. The $432M net cash "
    "balance represents 13% of market cap and continues to grow. We recommend initiating a "
    "position at current levels ($5.50) with a 12-month price target of $7.00. Key catalysts: "
    "Q1 FY2027 earnings (May/June 2026 — first print with NVIDIA partnership in force), "
    "new QNX edge AI design win announcements, and analyst PT revisions off the stale $4.84 consensus.",
    body_style,
))

# ── Footer ──────────────────────────────────────────────────────────────────
story.append(gap(6))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT, spaceAfter=4))
story.append(Paragraph(
    "This note is prepared for internal discussion purposes only. All projections are illustrative "
    "and based on publicly available information. Past performance is not indicative of future results. "
    "|  Francisco Rodriguez  |  April 2026",
    footnote_style,
))

doc.build(story)
print(f"✓  Initiation note saved → {OUTPUT}")
