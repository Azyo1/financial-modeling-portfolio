#!/usr/bin/env python3
"""
DKS LBO Deal Memo — Investment Memorandum PDF
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

OUTPUT = "/Users/paco/career/modeling-portfolio/dks-lbo/DKS_LBO_Deal_Memo.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=LETTER,
    leftMargin=0.80 * inch,
    rightMargin=0.80 * inch,
    topMargin=0.60 * inch,
    bottomMargin=0.60 * inch,
)

W = LETTER[0] - 1.60 * inch

# ── Colors ────────────────────────────────────────────────────────────────────
NAVY    = colors.HexColor("#1F3864")
NAVY2   = colors.HexColor("#2F5496")
DARK    = colors.HexColor("#1A1A1A")
MID     = colors.HexColor("#444444")
LIGHT   = colors.HexColor("#767676")
ROW_ALT = colors.HexColor("#F2F5FB")
ROW_HDR = colors.HexColor("#1F3864")
GRAY    = colors.HexColor("#F2F2F2")

# ── Styles ────────────────────────────────────────────────────────────────────

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

# ── Table helper ──────────────────────────────────────────────────────────────

def make_table(headers, rows, col_widths, zebra=True):
    data = [headers] + rows
    t = Table(data, colWidths=col_widths)
    style_cmds = [
        # Header row
        ("BACKGROUND",   (0, 0), (-1, 0), ROW_HDR),
        ("TEXTCOLOR",    (0, 0), (-1, 0), colors.white),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 8.5),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("BOTTOMPADDING",(0, 0), (-1, 0), 5),
        ("TOPPADDING",   (0, 0), (-1, 0), 5),
        # Data rows
        ("FONTNAME",     (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE",     (0, 1), (-1, -1), 8.5),
        ("ALIGN",        (1, 1), (-1, -1), "CENTER"),
        ("ALIGN",        (0, 1), (0, -1),  "LEFT"),
        ("TOPPADDING",   (0, 1), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 1), (-1, -1), 4),
        ("GRID",         (0, 0), (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
        ("LEFTPADDING",  (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]
    if zebra:
        for i in range(1, len(data)):
            if i % 2 == 0:
                style_cmds.append(("BACKGROUND", (0, i), (-1, i), ROW_ALT))
    t.setStyle(TableStyle(style_cmds))
    return t

# ══════════════════════════════════════════════════════════════════════════════
# BUILD STORY
# ══════════════════════════════════════════════════════════════════════════════

story = []

# ── TOP ACCENT BAR ────────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=4, color=NAVY, spaceAfter=8))

# ── MEMO HEADER ───────────────────────────────────────────────────────────────
header_data = [
    ["TO:",   "Investment Committee"],
    ["FROM:", "Francisco Rodriguez, Financial Analyst"],
    ["DATE:", "February 2026"],
    ["RE:",   "Leveraged Buyout of Dick's Sporting Goods, Inc. (NYSE: DKS)"],
]
for label, value in header_data:
    row_text = f"<b>{label}</b>  {value}"
    style = re_style if label == "RE:" else memo_header_style
    story.append(Paragraph(row_text, style))

story.append(gap(2))
story.append(Paragraph(
    "STRICTLY CONFIDENTIAL — FOR DISCUSSION PURPOSES ONLY",
    confidential_style,
))
story.append(gap(4))
story.append(HRFlowable(width="100%", thickness=0.75, color=NAVY, spaceAfter=8))

# ── EXECUTIVE SUMMARY ─────────────────────────────────────────────────────────
story += section("EXECUTIVE SUMMARY")
story.append(Paragraph(
    "We present a leveraged buyout of Dick's Sporting Goods, Inc. (DKS), the last major national "
    "big-box sporting goods retailer following the bankruptcies of Sports Authority (2016) and "
    "Modell's (2020). At an entry multiple of 9.0x LTM EBITDA, the transaction values DKS at a "
    "$15.3B enterprise value, funded with $9.4B of Term Loan B debt (5.5x leverage) and $5.9B of "
    "sponsor equity. The investment thesis centers on a private label mix shift that expands EBITDA "
    "margins from 13.1% to 16.5% over a 5-year hold, supported by aggressive free cash flow sweeps "
    "that deleverage the business from 5.5x at entry to approximately 2.4x at exit. At a 10.5x exit "
    "multiple — justified by materially improved earnings quality — the transaction delivers a "
    "<b>3.8x MOIC and 30.4% IRR</b> at Year 5.",
    body_style,
))

# ── COMPANY OVERVIEW ──────────────────────────────────────────────────────────
story += section("COMPANY OVERVIEW")

overview_headers = ["Metric", "LTM Value"]
overview_rows = [
    ["Revenue",         "$13,000M"],
    ["EBITDA",          "$1,700M"],
    ["EBITDA Margin",   "13.1%"],
    ["Stores",          "~850 locations"],
    ["Sector",          "Consumer Discretionary — Big-Box Sporting Goods"],
    ["HQ",              "Coraopolis, Pennsylvania"],
]
story.append(make_table(
    overview_headers, overview_rows,
    [W * 0.38, W * 0.62],
))
story.append(gap(6))
story.append(Paragraph(
    "DKS operates the largest specialty sporting goods retail platform in the United States, with "
    "broad assortment across team sports, fitness, outdoor, and footwear. Following the exit of all "
    "major national competitors, DKS has consolidated its market position and continues to invest in "
    "differentiated retail formats (Dick's House of Sport) and proprietary brand development "
    "(DSG, Alpine Design, Calia).",
    body_style,
))

# ── INVESTMENT THESIS ─────────────────────────────────────────────────────────
story += section("INVESTMENT THESIS")

drivers = [
    ("Market Consolidation",
     "DKS is the sole surviving national big-box platform in a $50B+ addressable market. "
     "Sports Authority (2016) and Modell's (2020) are gone with no credible replacement. "
     "Market share gains are structural and continue to accrete with each passing year."),
    ("Private Label Margin Expansion",
     "DSG and Alpine Design carry 500–800bps EBITDA margin premium versus national brands "
     "(Nike, Adidas, Under Armour). Growing private label penetration from ~15% toward 20%+ "
     "of revenue mix is the primary operational thesis, driving ~350bps of margin expansion "
     "across the hold period — from 13.1% at entry to 16.5% at exit."),
    ("Experiential Retail Differentiation",
     "The Dick's House of Sport flagship format — featuring climbing walls, batting cages, "
     "TrackMan golf simulators, and in-store services — drives materially higher average "
     "unit revenue and traffic that e-commerce competitors cannot replicate."),
    ("Cash Flow Deleveraging",
     "Aggressive free cash flow sweeps against the Term Loan B generate $3.4B in cumulative "
     "debt paydown across the hold period, reducing net debt from $9.4B to $5.5B. Compounding "
     "equity value creation through simultaneous EBITDA growth and debt reduction justifies "
     "the exit multiple re-rating to 10.5x."),
]
for title, desc in drivers:
    story += bl_bold(title, desc)
    story.append(gap(2))

# ── TRANSACTION STRUCTURE ─────────────────────────────────────────────────────
story += section("TRANSACTION STRUCTURE")

su_headers = ["Sources", "$M", "  ", "Uses", "$M"]
su_rows = [
    ["Term Loan B (5.5x)",  "$9,350",  "  ", "Equity Purchase Price",  "$15,000"],
    ["Revolver (drawn)",    "$0",      "  ", "Transaction Fees (2%)",  "$306"],
    ["Sponsor Equity",      "$5,956",  "  ", "",                       ""],
    ["Total Sources",       "$15,306", "  ", "Total Uses",             "$15,306"],
]
t = Table(su_rows, colWidths=[W*0.26, W*0.12, W*0.04, W*0.40, W*0.18])
t.setStyle(TableStyle([
    ("FONTNAME",     (0, 0), (-1, -2), "Helvetica"),
    ("FONTNAME",     (0, -1), (-1, -1), "Helvetica-Bold"),
    ("FONTSIZE",     (0, 0), (-1, -1), 8.5),
    ("ALIGN",        (1, 0), (1, -1),  "RIGHT"),
    ("ALIGN",        (4, 0), (4, -1),  "RIGHT"),
    ("TOPPADDING",   (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING",(0, 0), (-1, -1), 3),
    ("LEFTPADDING",  (0, 0), (-1, -1), 4),
    ("LINEBELOW",    (0, -2), (1, -2), 0.5, colors.HexColor("#AAAAAA")),
    ("LINEBELOW",    (3, -2), (4, -2), 0.5, colors.HexColor("#AAAAAA")),
    ("BACKGROUND",   (0, -1), (1, -1), GRAY),
    ("BACKGROUND",   (3, -1), (4, -1), GRAY),
]))
story.append(t)
story.append(gap(4))

debt_headers = ["Debt Tranche", "Amount", "Rate", "Amortization", "Maturity"]
debt_rows = [
    ["Term Loan B",           "$9,350M", "SOFR + 350bps (8.0%)", "1% per annum",  "7 years"],
    ["Revolving Credit Facility", "$750M capacity",  "SOFR + 275bps (7.25%)", "Bullet", "5 years"],
]
story.append(make_table(
    debt_headers, debt_rows,
    [W*0.22, W*0.16, W*0.22, W*0.20, W*0.20],
    zebra=False,
))

# ── FINANCIAL PROJECTIONS ─────────────────────────────────────────────────────
story += section("FINANCIAL PROJECTIONS  ($M)")

proj_headers = ["", "LTM", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
proj_rows = [
    ["Revenue",        "$13,000", "$13,520", "$14,061", "$14,764", "$15,502", "$16,277"],
    ["  Growth %",     "—",       "4.0%",    "4.0%",    "5.0%",    "5.0%",    "5.0%"],
    ["EBITDA",         "$1,700",  "$1,893",  "$2,109",  "$2,288",  "$2,480",  "$2,686"],
    ["  Margin %",     "13.1%",   "14.0%",   "15.0%",   "15.5%",   "16.0%",   "16.5%"],
    ["D&A",            "($351)",  "($365)",  "($380)",  "($399)",  "($419)",  "($440)"],
    ["EBIT",           "$1,349",  "$1,528",  "$1,729",  "$1,889",  "$2,061",  "$2,246"],
    ["Interest Exp.",  "—",       "($748)",  "($712)",  "($662)",  "($601)",  "($526)"],
    ["Net Income",     "—",       "$585",    "$763",    "$920",    "$1,095",  "$1,289"],
    ["Levered FCF",    "—",       "$355",    "$528",    "$672",    "$839",    "$1,025"],
    ["TLB Balance",    "$9,350",  "$8,902",  "$8,281",  "$7,516",  "$6,584",  "$5,464"],
]
cw = [W*0.18] + [W*0.82/6]*6
story.append(make_table(proj_headers, proj_rows, cw))
story.append(Paragraph(
    "Note: Interest computed on beginning-of-period balance. Cash sweep applied annually "
    "against all available levered free cash flow.",
    footnote_style,
))

# ── RETURNS ANALYSIS ──────────────────────────────────────────────────────────
story += section("RETURNS ANALYSIS")

ret_headers = ["", "Value"]
ret_rows = [
    ["Exit Year EBITDA",           "$2,686M"],
    ["Exit EV / EBITDA Multiple",  "10.5x"],
    ["Exit Enterprise Value",      "$28,203M"],
    ["Less: Net Debt at Exit",     "($5,464M)"],
    ["Less: Exit Fees (1%)",       "($282M)"],
    ["Equity Proceeds to Sponsor", "$22,457M"],
    ["Initial Equity Investment",  "$5,956M"],
    ["MOIC",                       "3.8x"],
    ["IRR (5-Year Hold)",          "30.4%"],
]
# Bold last 3 rows
t_ret = Table([ret_headers] + ret_rows, colWidths=[W*0.60, W*0.40])
t_ret.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0),  (-1, 0),  ROW_HDR),
    ("TEXTCOLOR",     (0, 0),  (-1, 0),  colors.white),
    ("FONTNAME",      (0, 0),  (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0),  (-1, -1), 8.5),
    ("FONTNAME",      (0, 1),  (-1, -1), "Helvetica"),
    ("FONTNAME",      (0, -2), (-1, -1), "Helvetica-Bold"),
    ("TEXTCOLOR",     (0, -2), (-1, -1), NAVY),
    ("ALIGN",         (1, 0),  (1, -1),  "RIGHT"),
    ("ALIGN",         (0, 1),  (0, -1),  "LEFT"),
    ("TOPPADDING",    (0, 0),  (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0),  (-1, -1), 4),
    ("LEFTPADDING",   (0, 0),  (-1, -1), 6),
    ("RIGHTPADDING",  (0, 0),  (-1, -1), 6),
    ("GRID",          (0, 0),  (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
    ("BACKGROUND",    (0, 7),  (-1, 8),  GRAY),
    ("LINEABOVE",     (0, 7),  (-1, 7),  0.5, NAVY2),
    ("LINEBELOW",     (0, 9),  (-1, 9),  1.0, NAVY),
]))
story.append(t_ret)

# ── SENSITIVITY ───────────────────────────────────────────────────────────────
story += section("SENSITIVITY — IRR BY EXIT MULTIPLE SCENARIO")

sens_headers = ["Scenario", "Exit Multiple", "Exit TEV", "Net Debt", "Equity Proceeds", "MOIC", "IRR"]
sens_rows = [
    ["Bull Case",        "11.0x", "$29,546M", "$5,464M", "$23,800M", "4.0x", "33.0%"],
    ["Base Case ★",     "10.5x", "$28,203M", "$5,464M", "$22,457M", "3.8x", "30.4%"],
    ["Conservative",     "9.0x",  "$24,174M", "$5,464M", "$18,428M", "3.1x", "25.2%"],
    ["Downside",         "7.0x",  "$18,802M", "$5,464M", "$13,056M", "2.2x", "17.1%"],
    ["Stress",           "6.0x",  "$16,116M", "$5,464M", "$10,370M", "1.7x", "11.7%"],
]
story.append(make_table(
    sens_headers, sens_rows,
    [W*0.18, W*0.12, W*0.14, W*0.12, W*0.18, W*0.10, W*0.10] + [0],
    zebra=False,
))
story.append(Paragraph(
    "★ Base case assumes entry at 9.0x, exit at 10.5x reflecting business quality improvement "
    "from private label margin expansion. Net debt held constant at Year 5 base case level.",
    footnote_style,
))

# ── KEY RISKS ─────────────────────────────────────────────────────────────────
story += section("KEY RISKS & MITIGANTS")

risks = [
    ("Private Label Thesis Failure",
     "If DSG / Alpine Design fail to gain traction and consumers remain loyal to national brands, "
     "EBITDA margins remain flat at ~13%. At 9.0x / 9.0x with no margin expansion, IRR falls to "
     "~21%. Mitigant: private label penetration is already tracking above 15% and accelerating; "
     "DKS controls shelf space allocation."),
    ("Floating Rate Exposure",
     "The $9.4B TLB is priced at SOFR + 350bps. A 150bps SOFR increase adds ~$141M of annual "
     "interest, reducing free cash flow and slowing debt sweeps. Mitigant: strong FCF generation "
     "provides meaningful buffer; interest rate hedges are standard practice on large TLBs."),
    ("Consumer Discretionary Cycle",
     "DKS is 100% consumer discretionary. A recession compresses traffic and ticket simultaneously "
     "at peak leverage. Mitigant: DKS's consolidation-driven market position means they gain share "
     "even in downturns; 5.5x leverage provides more cushion than the 7x+ that failed at Sports "
     "Authority."),
    ("Multiple Compression",
     "Entry at 9.0x with a 10.5x exit assumption requires some re-rating. If markets de-rate "
     "consumer retail and exit is forced at 7.0x, IRR falls to ~17%. Mitigant: EBITDA growth and "
     "cash sweeps provide substantial cushion; the deal returns equity at 7.0x exit."),
]
for title, desc in risks:
    story += bl_bold(title, desc)
    story.append(gap(1))

# ── RECOMMENDATION ────────────────────────────────────────────────────────────
story += section("RECOMMENDATION")
story.append(Paragraph(
    "We recommend proceeding with the leveraged buyout of Dick's Sporting Goods at an entry "
    "multiple of 9.0x LTM EBITDA. The transaction offers a differentiated thesis anchored in "
    "structural market consolidation and a clear operational playbook — private label margin "
    "expansion — that is already in motion. The deal generates meaningful returns across a wide "
    "range of exit scenarios (17%+ IRR even at a 7.0x exit multiple), and the cash sweep "
    "mechanism creates compounding equity value creation that is not dependent on financial "
    "engineering alone. We recommend authorization to proceed to exclusivity.",
    body_style,
))

# ── FOOTER RULE ───────────────────────────────────────────────────────────────
story.append(gap(6))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT, spaceAfter=4))
story.append(Paragraph(
    "This memorandum is prepared for internal discussion purposes only. All projections are "
    "illustrative and based on publicly available information. Past performance is not indicative "
    "of future results.  |  Francisco Rodriguez  |  February 2026",
    footnote_style,
))

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"✓  Deal memo saved → {OUTPUT}")
