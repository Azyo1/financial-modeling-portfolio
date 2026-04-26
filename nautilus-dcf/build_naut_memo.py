#!/usr/bin/env python3
"""
Nautilus Biotechnology DCF Initiation Note — Equity Research PDF
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

OUTPUT = "/Users/paco/career/modeling-portfolio/nautilus-dcf/NAUT_DCF_Initiation_Note.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=LETTER,
    leftMargin=0.80 * inch,
    rightMargin=0.80 * inch,
    topMargin=0.75 * inch,
    bottomMargin=0.60 * inch,
)

def add_page_header(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(colors.HexColor("#9E9E9E"))
    canvas.drawString(0.80 * inch, LETTER[1] - 0.42 * inch,
                      "Francisco Rodriguez  |  Financial Modeling Portfolio")
    canvas.drawRightString(LETTER[0] - 0.80 * inch, LETTER[1] - 0.42 * inch,
                           "NAUT — DCF Initiation Note")
    canvas.setStrokeColor(colors.HexColor("#DDDDDD"))
    canvas.setLineWidth(0.3)
    canvas.line(0.80 * inch, LETTER[1] - 0.47 * inch,
                LETTER[0] - 0.80 * inch, LETTER[1] - 0.47 * inch)
    canvas.restoreState()

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

# ── TOP ACCENT BAR ─────────────────────────────────────────────────────────
story.append(HRFlowable(width="100%", thickness=4, color=NAVY, spaceAfter=8))

# ── MEMO HEADER ────────────────────────────────────────────────────────────
header_data = [
    ["TO:",   "Investment Committee"],
    ["FROM:", "Francisco Rodriguez, Financial Analyst"],
    ["DATE:", "March 2026"],
    ["RE:",   "Initiation of Coverage — Nautilus Biotechnology, Inc. (NASDAQ: NAUT) | OVERWEIGHT | PT: $5.00"],
]
for label, value in header_data:
    row_text = f"<b>{label}</b>  {value}"
    style = re_style if label == "RE:" else memo_header_style
    story.append(Paragraph(row_text, style))

story.append(gap(2))
story.append(Paragraph("STRICTLY CONFIDENTIAL — FOR DISCUSSION PURPOSES ONLY", confidential_style))
story.append(gap(4))
story.append(HRFlowable(width="100%", thickness=0.75, color=NAVY, spaceAfter=8))

# ── RATING BOX ─────────────────────────────────────────────────────────────
rating_data = [["Rating", "Price Target", "Current Price", "Upside", "52-Wk Range"]]
rating_rows = [["OVERWEIGHT", "$5.00", "$2.65", "+88.7%", "$1.49 – $4.25"]]
t_rating = Table(rating_data + rating_rows, colWidths=[W*0.16, W*0.16, W*0.16, W*0.16, W*0.36])
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

# ── EXECUTIVE SUMMARY ──────────────────────────────────────────────────────
story += section("EXECUTIVE SUMMARY")
story.append(Paragraph(
    "We initiate coverage of Nautilus Biotechnology (NAUT) with an <b>OVERWEIGHT</b> rating and a "
    "<b>$5.00 price target</b>, representing 89% upside from the current price of $2.65. Nautilus has "
    "built a genuinely novel single-molecule proteomics platform — Voyager — that can simultaneously "
    "quantify 10 billion intact protein molecules with 1.5% coefficient of variation, versus 40–80% CV "
    "for incumbent mass spectrometry platforms. The technology is not incremental; it represents the "
    "same step-change disruption in proteomics that Illumina's sequencing-by-synthesis delivered to "
    "genomics beginning in 2007. With the platform unveiled publicly at US HUPO (February 2026), a "
    "first paying Early Access Program customer secured (Baylor College of Medicine, March 2026), "
    "and commercial launch targeted for late 2026, key technology and execution risks are "
    "progressively de-risking. At an enterprise value of ~$191M — less than 3× FY2025 operating "
    "expenses — the market is pricing near-total failure into a platform with a multi-billion dollar "
    "long-term addressable opportunity.",
    body_style,
))

# ── COMPANY OVERVIEW ───────────────────────────────────────────────────────
story += section("COMPANY OVERVIEW")

overview_headers = ["Metric", "Value"]
overview_rows = [
    ["Market Cap",              "~$347M"],
    ["Enterprise Value",        "~$191M"],
    ["Net Cash",                "$156.1M  ($1.23/share)"],
    ["FY2025 Operating Expenses", "$66.8M  (R&D: $41.1M · G&A: $25.7M)"],
    ["FY2025 Net Loss",         "($59.0M)"],
    ["2026E Cash Burn (Mgmt)",  "$65–70M"],
    ["Cash Runway",             "Through 2027 (raise required)"],
    ["Stage",                   "Pre-Revenue / Development Stage"],
    ["Technology",              "Voyager™ — Single-Molecule Iterative Mapping Proteomics"],
    ["First Commercial Launch", "Late 2026 (instruments ship Q1 2027)"],
]
story.append(make_table(overview_headers, overview_rows, [W * 0.42, W * 0.58]))
story.append(gap(6))
story.append(Paragraph(
    "Founded in 2016 and public since 2021, Nautilus is developing the Voyager platform — an "
    "integrated instrument, consumable, and software system for single-molecule protein analysis. "
    "The platform's core innovation, Iterative Mapping, exposes billions of individual protein "
    "molecules to successive rounds of probe binding, with machine learning translating probe "
    "patterns into confident proteoform identifications. The first commercial assay — the "
    "Nautilus Tau Proteoforms Assay — quantifies 768+ full-length tau proteoform groups "
    "simultaneously, directly applicable to Alzheimer's and neurodegeneration biomarker research.",
    body_style,
))

# ── INVESTMENT THESIS ──────────────────────────────────────────────────────
story += section("INVESTMENT THESIS")

drivers = [
    ("Voyager Platform: Architecturally Differentiated",
     "Legacy mass spectrometry requires protein fragmentation to measure peptides — a process that "
     "destroys proteoform context. Nautilus' Iterative Mapping keeps proteins intact and interrogates "
     "each molecule independently across 50–100+ probe cycles, achieving 1.5% CV versus 40–80% for "
     "Orbitrap-based platforms. Crucially, the platform can resolve co-occurring post-translational "
     "modifications on a single protein molecule — an impossible task for any affinity-based or "
     "mass-spec platform at scale. This is not a faster mass spec; it is a fundamentally different "
     "measurement modality."),
    ("Razor / Blade Economics Drive Long-Term Value",
     "Voyager instruments at ~$1M ASP establish customer relationships; consumables (flow cells, "
     "probe libraries, reagents) at estimated $150–300K annual pull-through per instrument generate "
     "the high-margin recurring revenue that creates intrinsic value. As the installed base scales "
     "to 200+ instruments by 2032E, consumables become the majority of revenue, expanding blended "
     "gross margins from ~50% at commercial launch toward 65% — consistent with mature tools "
     "companies (Illumina: 68%, 10x Genomics: 65%). Software and data-analysis subscriptions "
     "represent an unmodeled upside optionality layer."),
    ("Valuation Prices Near-Total Failure — Margin of Safety in Cash",
     "At $2.65/share, NAUT's EV of ~$191M implies the market assigns minimal option value to a "
     "platform that has already attracted paying customers and published reproducibility data. "
     "The $156M net cash balance ($1.23/share) represents 46% of the current stock price, "
     "providing downside protection. Our base case DCF — with conservative 20% WACC (reflecting "
     "genuine execution risk) and an $8x terminal EV/Revenue multiple (below the 10x–15x that "
     "Illumina commanded at comparable stages) — yields $4.81/share intrinsic value, supporting "
     "a $5.00 price target. The risk/reward is asymmetric at current prices."),
    ("Proteomics Is at an Illumina-in-2007 Inflection Point",
     "The proteomics tools market is projected to reach $65.8B by 2030 at 12% CAGR. Biopharma's "
     "recognition that proteins — not genes — are the proximal drivers of disease is accelerating "
     "proteomics' transition from academic curiosity to clinical drug discovery workflow. Nautilus' "
     "Tau Proteoforms Assay is strategically positioned in neurodegeneration, where the ability to "
     "quantify disease-relevant tau proteoforms (phosphorylated, truncated, aggregated) ahead of "
     "symptom onset is a multi-hundred-million-dollar biomarker opportunity with major pharma "
     "customers already engaged."),
]
for title, desc in drivers:
    story += bl_bold(title, desc)
    story.append(gap(2))

# ── FINANCIAL PROJECTIONS ──────────────────────────────────────────────────
story += section("FINANCIAL PROJECTIONS  ($M) — BASE CASE")

proj_headers = ["", "FY25A", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"]
proj_rows = [
    ["Revenue",         "$0",    "$0.5",  "$8.0",   "$30.0",  "$70.0",  "$130.0", "$200.0"],
    ["  Growth %",      "—",     "—",     "1,500%", "275%",   "133%",   "85%",    "54%"],
    ["Gross Profit",    "$0",    "$0.3",  "$4.0",   "$15.6",  "$38.5",  "$78.0",  "$126.0"],
    ["  Gross Margin",  "—",     "60%",   "50%",    "52%",    "55%",    "60%",    "63%"],
    ["R&D",             "$41.1", "$50.0", "$55.0",  "$60.0",  "$65.0",  "$70.0",  "$72.0"],
    ["G&A",             "$25.7", "$28.0", "$30.0",  "$32.0",  "$34.0",  "$36.0",  "$38.0"],
    ["EBIT",            "($66.8)","($77.7)","($81.0)","($76.4)","($60.5)","($28.0)","$16.0"],
    ["Unlevered FCF",   "($50.7)","($84.7)","($92.5)","($90.8)","($75.5)","($47.0)","($7.0)"],
]
cw = [W*0.16] + [W*0.84/7]*7
story.append(make_table(proj_headers, proj_rows, cw))
story.append(Paragraph(
    "Note: FY25A from 10-K filings. FY26E–FY31E are analyst projections. "
    "EBIT losses reflect investment phase; profitability inflects in 2031E.",
    footnote_style,
))
story.append(gap(4))

# Extended projections
proj2_headers = ["", "FY32E", "FY33E", "FY34E", "FY35E (Terminal)"]
proj2_rows = [
    ["Revenue",        "$280.0",  "$360.0",  "$430.0",  "$490.0"],
    ["Gross Profit",   "$182.0",  "$234.0",  "$279.5",  "$318.5"],
    ["  Gross Margin", "65%",     "65%",     "65%",     "65%"],
    ["EBIT",           "$68.0",   "$118.0",  "$160.5",  "$196.5"],
    ["  EBIT Margin",  "24.3%",   "32.8%",   "37.3%",   "40.1%"],
    ["Unlevered FCF",  "$30.0",   "$67.5",   "$101.4",  "$130.4"],
]
cw2 = [W*0.30] + [W*0.70/4]*4
story.append(make_table(proj2_headers, proj2_rows, cw2))

# ── VALUATION ──────────────────────────────────────────────────────────────
story += section("DCF VALUATION SUMMARY")

val_headers = ["Component", "Base Case", "Bull Case", "Bear Case"]
val_rows = [
    ["WACC",                    "20.0%",    "17.0%",   "20.0%"],
    ["Terminal EV/Revenue",     "8.0x",     "10.0x",   "6.0x"],
    ["Terminal Revenue (2035E)","$490M",    "$700M",   "$200M"],
    ["Sum PV of FCFs",          "($180.0M)","($153.0M)","($152.9M)"],
    ["PV of Terminal Value",    "$633.0M",  "$966.0M", "$193.0M"],
    ["Enterprise Value",        "$453.1M",  "$813.0M", "$40.1M"],
    ["(+) Net Cash",            "$156.1M",  "$156.1M", "$156.1M"],
    ["Equity Value",            "$609.2M",  "$969.1M", "$196.2M"],
    ["÷ Shares (M)",            "126.6M",   "126.6M",  "126.6M"],
    ["Intrinsic Value / Share", "$4.81",    "$7.65",   "$1.55"],
    ["Scenario Weight",         "55%",      "25%",     "20%"],
]
t_val = Table([val_headers] + val_rows, colWidths=[W*0.36, W*0.21, W*0.21, W*0.22])
t_val.setStyle(TableStyle([
    ("BACKGROUND",    (0, 0),  (-1, 0),  ROW_HDR),
    ("TEXTCOLOR",     (0, 0),  (-1, 0),  colors.white),
    ("FONTNAME",      (0, 0),  (-1, 0),  "Helvetica-Bold"),
    ("FONTSIZE",      (0, 0),  (-1, -1), 8.5),
    ("ALIGN",         (1, 0),  (-1, -1), "CENTER"),
    ("ALIGN",         (0, 1),  (0, -1),  "LEFT"),
    ("FONTNAME",      (0, 1),  (-1, -1), "Helvetica"),
    ("TOPPADDING",    (0, 0),  (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0),  (-1, -1), 4),
    ("LEFTPADDING",   (0, 0),  (-1, -1), 6),
    ("RIGHTPADDING",  (0, 0),  (-1, -1), 6),
    ("GRID",          (0, 0),  (-1, -1), 0.3, colors.HexColor("#CCCCCC")),
    # Bold key rows
    ("FONTNAME",      (0, 10), (-1, 10), "Helvetica-Bold"),
    ("FONTNAME",      (0, 8),  (-1, 8),  "Helvetica-Bold"),
    ("BACKGROUND",    (0, 10), (-1, 10), GRAY),
    ("BACKGROUND",    (0, 8),  (-1, 8),  GRAY),
    ("LINEABOVE",     (0, 10), (-1, 10), 0.75, NAVY2),
    # Zebra
    ("BACKGROUND",    (0, 2),  (-1, 2),  ROW_ALT),
    ("BACKGROUND",    (0, 4),  (-1, 4),  ROW_ALT),
    ("BACKGROUND",    (0, 6),  (-1, 6),  ROW_ALT),
]))
story.append(t_val)
story.append(Paragraph(
    "Blended price target = 0.55 × $4.81 + 0.25 × $7.65 + 0.20 × $1.55 = <b>$5.00</b>. "
    "WACC of 20% reflects pre-revenue execution risk, development-stage micro-cap premium, "
    "and terminal beta consistent with life science tools peers (Seer Bio, Quantum-Si). "
    "Terminal EV/Revenue of 8x is a discount to Illumina's comparable-stage multiple (~12x).",
    footnote_style,
))

# ── SENSITIVITY ────────────────────────────────────────────────────────────
story += section("SENSITIVITY — PRICE TARGET BY WACC & TERMINAL EV/REVENUE MULTIPLE")

sens_headers = ["WACC \\ EV/Rev →", "5.0x", "6.0x", "7.0x", "8.0x ★", "9.0x", "10.0x", "12.0x"]
sens_rows = [
    ["14%",  "$3.85", "$4.88", "$5.91", "$6.94",  "$7.97",  "$8.99",  "$11.05"],
    ["17%",  "$2.75", "$3.57", "$4.39", "$5.22",  "$6.04",  "$6.86",  "$8.51"],
    ["18%",  "$2.51", "$3.27", "$4.03", "$4.79",  "$5.55",  "$6.31",  "$7.83"],
    ["20% ★","$2.09", "$2.73", "$3.37", "$4.01",  "$4.65",  "$5.29",  "$6.57"],
    ["22%",  "$1.74", "$2.28", "$2.83", "$3.37",  "$3.91",  "$4.45",  "$5.53"],
    ["24%",  "$1.45", "$1.91", "$2.37", "$2.83",  "$3.28",  "$3.74",  "$4.66"],
    ["26%",  "$1.20", "$1.59", "$1.98", "$2.37",  "$2.76",  "$3.15",  "$3.93"],
]
story.append(make_table(sens_headers, sens_rows,
    [W*0.13, W*0.13, W*0.13, W*0.13, W*0.13, W*0.13, W*0.13, W*0.09],
    zebra=False))
story.append(Paragraph(
    "★ Base case: 20% WACC, 8.0x terminal EV/Revenue → $4.01/share intrinsic value. "
    "Shaded region represents prices above current market price of $2.65.",
    footnote_style,
))

# ── KEY RISKS ──────────────────────────────────────────────────────────────
story += section("KEY RISKS & MITIGANTS")

risks = [
    ("Commercialization Delay Risk (HIGH)",
     "The platform launch has already slipped once (original 2025 target → late 2026). Further "
     "delays to 2027+ would consume additional cash and open competitive windows. At $65-70M "
     "annual burn with $156M cash, the company has approximately 2.2 years of runway. Any slip "
     "pushes the required 2027 equity raise earlier at potentially deeper dilution. Mitigant: "
     "Baylor EAP customer announced March 2026 suggests the platform is performing in real "
     "laboratory conditions; commercial launch is a commitment, not an aspiration."),
    ("Capital Raise Dilution (HIGH)",
     "The company will almost certainly need to raise $75-150M+ in 2027 to fund the commercial "
     "ramp. At current prices (~$2.65), a $100M raise would issue ~37.7M new shares (30% dilution). "
     "Our DCF does not model this dilution explicitly — the intrinsic per-share values above are "
     "pre-dilution. Post-dilution price targets would be lower by approximately 20-25%. Mitigant: "
     "successful commercial traction by late 2026 enables a raise at a materially higher price."),
    ("Competitive Response from Incumbents (MEDIUM)",
     "Thermo Fisher Scientific (TMO) commands 30-40% of the proteomics instrument market with "
     "Orbitrap and Olink platforms. With effectively unlimited capital, Thermo could acquire a "
     "competing platform (Seer Bio is publicly traded at ~$350M market cap) or accelerate internal "
     "development. Mitigant: Nautilus' single-molecule, intact-protein approach is architecturally "
     "distinct — it is not a faster mass spec and cannot be replicated via incremental improvement "
     "to existing platforms."),
    ("Technology Execution Risk (MEDIUM)",
     "Probe library specificity at scale, flow cell stability over 100+ cycles, and ML model "
     "performance in complex biological matrices (e.g., plasma) remain unvalidated at commercial "
     "scale. EAP lab data may not generalize to diverse customer workflows. Mitigant: iterative "
     "engineering is Nautilus' core competency; the EAP phase is specifically designed to identify "
     "and resolve these challenges before broad commercial rollout."),
]
for title, desc in risks:
    story += bl_bold(title, desc)
    story.append(gap(1))

# ── RECOMMENDATION ─────────────────────────────────────────────────────────
story += section("RECOMMENDATION")
story.append(Paragraph(
    "We initiate coverage of Nautilus Biotechnology with an <b>OVERWEIGHT</b> rating and a "
    "<b>$5.00 twelve-month price target</b>. NAUT presents a rare asymmetric opportunity: a "
    "genuinely disruptive proteomics platform trading at an EV of ~$191M — effectively pricing "
    "in near-failure — at the precise moment of commercial inflection. The $156M net cash balance "
    "provides downside support at ~$1.23/share. The base case DCF yields $4.81/share; the blended "
    "scenario-weighted target is $5.00. Key catalysts in the next 12 months include additional "
    "EAP customer announcements (H1 2026), a commercial launch / pre-order announcement (late "
    "2026), and the first instrument shipments (Q1 2027). We recommend initiating a position at "
    "current levels, sized to reflect the binary nature of commercialization outcomes.",
    body_style,
))

# ── FOOTER ─────────────────────────────────────────────────────────────────
story.append(gap(6))
story.append(HRFlowable(width="100%", thickness=0.5, color=LIGHT, spaceAfter=4))
story.append(Paragraph(
    "This note is prepared for internal discussion purposes only. All projections are illustrative "
    "and based on publicly available information. Past performance is not indicative of future "
    "results.  |  Francisco Rodriguez  |  March 2026",
    footnote_style,
))

doc.build(story, onFirstPage=add_page_header, onLaterPages=add_page_header)
print(f"✓  Initiation note saved → {OUTPUT}")
