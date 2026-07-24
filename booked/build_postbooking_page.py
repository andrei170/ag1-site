"""
Build the AG1 post-booking page (ag1consulting.co/booked/).

This file lives in the ag1-site repo, in booked/, and writes index.html next to
itself. ag1-site is the repo that holds the CNAME for ag1consulting.co, so this
is the only copy that reaches the live URL. The separate ag1-postbooking repo is
an older duplicate that serves at andrei170.github.io/ag1-postbooking/ and does
not feed the live page. Do not edit that one expecting /booked/ to change.

Images in assets/ are base64 inlined, so the output is a single ~3.4MB index.html
with no external image requests. GitHub Pages takes a few minutes to flip the
cache on a file that size, so curl before telling anyone it is live.

Usage:
    python build_postbooking_page.py

Editing notes:
    - BREAKOUT_VIDEOS: set "loom" to a Loom share id once a clip is filmed and the
      card turns from a placeholder into a real link. Nothing else to change.
    - PROOF and DEMOS are plain lists. Delete an entry to drop a tile.
"""
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
OUT = os.path.join(HERE, "index.html")

LOOM_MAIN = "9a4149d29c8d4f3f998eda6c3f45719f"
SMS_NUMBER = "+44 7846 715676"
SMS_TEL = "+447846715676"

# ---------------------------------------------------------------- breakout videos
# One card per objection, ranked as they appeared in the recorded sales calls.
# Titled as the prospect would ask it. loom=None renders a "being filmed" placeholder.
BREAKOUT_VIDEOS = [
    {
        "icon": "mdi:fire-alert",
        "q": "I have been burned by an agency before",
        "teaser": "Why the lead-selling model produces the horror stories, and what we do instead of it.",
        "loom": None,
    },
    {
        "icon": "mdi:calculator-variant-outline",
        "q": "Will this actually work at my margin?",
        "teaser": "The ad spend sum run properly, and the two honest ways round a thin margin.",
        "loom": None,
    },
    {
        "icon": "mdi:account-tie-outline",
        "q": "Who actually are you?",
        "teaser": "AG1 Consulting Ltd, registered in England and Wales, founder-led. Where to go and check.",
        "loom": None,
    },
    {
        "icon": "mdi:vector-difference",
        "q": "What makes you different from the last lot?",
        "teaser": "The site, the search and the ads run as one system, with the follow-up built in behind it.",
        "loom": None,
    },
    {
        "icon": "mdi:calendar-clock-outline",
        "q": "I am already flat out, I cannot take more on",
        "teaser": "Being too busy is usually a reason to have this conversation, not a reason to skip it.",
        "loom": None,
    },
    {
        "icon": "mdi:filter-check-outline",
        "q": "How do I know they will not be time-wasters?",
        "teaser": "Where the qualifying happens, and why it happens before your phone ever rings.",
        "loom": None,
    },
    {
        "icon": "mdi:timer-sand",
        "q": "How long until I see anything?",
        "teaser": "Honest timelines. The site and the follow-up work straight away. Search takes months.",
        "loom": None,
    },
    {
        "icon": "mdi:clipboard-check-outline",
        "q": "What do I actually have to do?",
        "teaser": "Close to nothing. We build it. You keep answering the phone the way you already do.",
        "loom": None,
    },
    {
        "icon": "mdi:cash-multiple",
        "q": "What is this going to cost me?",
        "teaser": "The shape of the pricing, setup fee included, so nobody gets ambushed with a number.",
        "loom": None,
    },
    {
        "icon": "mdi:gesture-tap-button",
        "q": "I am not technical, will I be able to use it?",
        "teaser": "You will not be asked to learn any software. That is the entire point of hiring us.",
        "loom": None,
    },
]

# ---------------------------------------------------------------- come-ready checklist
CHECKLIST = [
    ("mdi:calendar-check-outline", "Accept the calendar invite",
     "Check your inbox and hit accept so it does not get buried."),
    ("mdi:clock-outline", "Block out about 45 minutes",
     "We go deep on this. A rushed 20 minutes helps neither of us."),
    ("mdi:volume-off", "Be somewhere quiet",
     "And camera on, please. Not on the way to a job."),
    ("mdi:wifi-strength-4", "Get a strong wifi connection",
     "We will be sharing our screen with you for most of it."),
    ("mdi:chart-box-outline", "Have your rough numbers handy",
     "Enquiries a month, and what an average job is worth to you. Rough is fine."),
    ("mdi:account-multiple-outline", "Bring whoever else decides",
     "If a partner or a manager is in on the decision, get them on the call too."),
]

# ---------------------------------------------------------------- proof grid
PROOF = [
    ("proof-01-klaviyo-total.png", "$11.59M total revenue",
     "For a brand we run the marketing for (Klaviyo)."),
    ("proof-02-accounts.png", "$5.8M accounts",
     "Email &amp; SMS revenue across multiple client accounts."),
    ("proof-03-stripe-growth.png", "$50k/yr &rarr; $100k/mo",
     "From $50k a year online to $50-100k a month - $331K in 6 months (Stripe)."),
    ("proof-04-stripe-5x.png", "5X in a year",
     "From $24,947 to $126K per month - 5X growth in 12 months (Stripe)."),
    ("proof-05-ads-742k.png", "$742K in 6 months",
     "$742K in revenue in 6 months from the ads we run."),
    ("proof-06-klaviyo-932k.png", "$932K in a period",
     "$932K driven through email &amp; SMS - 15.88% of a $5.8M brand's revenue (Klaviyo)."),
    ("proof-07-klaviyo-98k.png", "$98K/mo from email",
     "Up to $98K a month from the email flows we run (Klaviyo)."),
]

# ---------------------------------------------------------------- work grid
DEMOS = [
    ("demo-01-fluid-roofing.jpg", "https://andrei170.github.io/fluid-roofing/",
     "WEBSITE", "Roofing", "A roofing site built to actually book jobs.", "View the site"),
    ("demo-02-fox-view-dental.jpg", "https://andrei170.github.io/fox-view-dental-site/",
     "WEBSITE", "Dental", "A dental practice site built to fill the calendar.", "View the site"),
    ("demo-03-ablaze-audit.jpg", "https://andrei170.github.io/ablaze-aesthetics-site/audit.html",
     "AUDIT", "Med spa", "A graded audit of a med spa's online presence.", "View the audit"),
    ("demo-04-benavides-audit.jpg", "https://andrei170.github.io/benavides-law-site/audit.html",
     "AUDIT", "Law firm", "An SEO audit showing a firm's revenue at stake.", "View the audit"),
]


def data_uri(filename):
    path = os.path.join(ASSETS, filename)
    mime = "image/png" if filename.lower().endswith(".png") else "image/jpeg"
    with open(path, "rb") as f:
        return f"data:{mime};base64,{base64.b64encode(f.read()).decode('ascii')}"


def render_videos():
    out = []
    for i, v in enumerate(BREAKOUT_VIDEOS, start=1):
        num = f"{i:02d}"
        if v["loom"]:
            tag = "a"
            attrs = (f' href="https://www.loom.com/share/{v["loom"]}"'
                     ' target="_blank" rel="noopener"')
            badge = '<span class="vbadge live">Watch</span>'
            cls = "vcard live"
        else:
            tag = "article"
            attrs = ""
            badge = '<span class="vbadge">Filming this week</span>'
            cls = "vcard"
        out.append(f"""    <{tag} class="{cls}"{attrs}>
      <div class="vthumb">
        <iconify-icon class="vicon" icon="{v['icon']}"></iconify-icon>
        <span class="vplay" aria-hidden="true"></span>
        {badge}
      </div>
      <div class="vbody">
        <span class="vnum">{num}</span>
        <h3>{v['q']}</h3>
        <p>{v['teaser']}</p>
      </div>
    </{tag}>""")
    return "\n".join(out)


def render_checklist():
    return "\n".join(
        f"""        <li>
          <iconify-icon class="cicon" icon="{icon}"></iconify-icon>
          <div><b>{title}</b><span>{body}</span></div>
        </li>""" for icon, title, body in CHECKLIST)


def render_proof():
    return "\n".join(
        f'    <figure class="shot"><img src="{data_uri(f)}" alt="{cap}">'
        f"<figcaption><b>{head}</b><span>{cap}</span></figcaption></figure>"
        for f, head, cap in PROOF)


def render_demos():
    return "\n".join(
        f"""    <a class="demo" href="{href}" target="_blank" rel="noopener">
      <div class="demo-thumb"><img src="{data_uri(f)}" alt="{title} {tag.lower()}"></div>
      <div class="demo-body"><span class="demo-tag">{tag}</span><h3>{title}</h3>
        <p>{blurb}</p><span class="demo-link">{cta} &rarr;</span></div>
    </a>""" for f, href, tag, title, blurb, cta in DEMOS)


HTML = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&display=swap');
:root{{--gold:#C9973A;--gold-bright:#E0BC63;--gold-deep:#B8922E;--bg:#050506;--panel:#0C0C11;
--line:rgba(201,151,58,.2);--line2:rgba(201,151,58,.4);--text:#F5F2EB;--mute:#B7B2A7;--deep:#7E7A70;
--serif:'Cormorant Garamond',Georgia,serif;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,sans-serif;--mono:ui-monospace,Consolas,monospace;}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:var(--bg);color:var(--text);font-family:var(--sans);line-height:1.6;
background-image:radial-gradient(900px 480px at 82% -6%,rgba(201,151,58,.1),transparent 60%),radial-gradient(760px 440px at 6% 3%,rgba(201,151,58,.06),transparent 60%);background-attachment:fixed}}
.topbar{{position:fixed;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,var(--gold-deep),var(--gold-bright)50%,var(--gold-deep));z-index:10}}
.wrap{{max-width:1000px;margin:0 auto;padding:0 24px}}
.eye{{font-family:var(--mono);font-size:12px;letter-spacing:4px;text-transform:uppercase;color:var(--gold);margin-bottom:18px}}
.hero{{padding:100px 0 26px;text-align:center}}
.logo{{font-family:var(--serif);font-weight:700;font-size:22px;margin-bottom:40px}}
.logo b{{color:var(--gold)}}
.chip{{display:inline-block;padding:7px 16px;border:1px solid var(--line2);border-radius:999px;background:rgba(201,151,58,.1);color:var(--gold-bright);font-family:var(--mono);font-size:12px;letter-spacing:2px;text-transform:uppercase;margin-bottom:24px}}
h1{{font-family:var(--serif);font-weight:700;font-size:clamp(2.6rem,6vw,4.4rem);line-height:1.02;letter-spacing:-.5px;margin-bottom:16px}}
h1 em{{font-style:italic;color:var(--gold-bright)}}
.lede{{color:var(--mute);font-size:clamp(16px,1.9vw,20px);max-width:56ch;margin:0 auto}}
section{{padding:46px 0}}
h2{{font-family:var(--serif);font-weight:700;font-size:clamp(1.8rem,3.6vw,2.6rem);text-align:center;margin-bottom:8px}}
h2 em{{font-style:italic;color:var(--gold-bright)}}
.sub{{color:var(--mute);text-align:center;max-width:52ch;margin:0 auto 30px}}
.sub a{{color:var(--gold-bright)}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
@media(max-width:760px){{.grid{{grid-template-columns:1fr}}}}

/* breakout video cards */
.vgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:18px}}
.vcard{{display:flex;flex-direction:column;background:linear-gradient(150deg,rgba(201,151,58,.06),rgba(0,0,0,.3));
border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;color:inherit;transition:.18s}}
.vcard.live:hover{{border-color:var(--line2);transform:translateY(-3px)}}
.vthumb{{position:relative;aspect-ratio:16/9;display:flex;align-items:center;justify-content:center;
border-bottom:1px solid var(--line);background:
radial-gradient(420px 200px at 50% 120%,rgba(201,151,58,.16),transparent 70%),
linear-gradient(150deg,rgba(201,151,58,.1),rgba(0,0,0,.55))}}
.vicon{{font-size:44px;color:var(--gold);opacity:.75}}
.vplay{{position:absolute;right:14px;bottom:14px;width:34px;height:34px;border-radius:50%;
background:var(--gold);display:flex;align-items:center;justify-content:center;box-shadow:0 6px 20px rgba(201,151,58,.35)}}
.vplay:after{{content:"";border-left:11px solid #000;border-top:7px solid transparent;border-bottom:7px solid transparent;margin-left:3px}}
.vbadge{{position:absolute;left:12px;top:12px;font-family:var(--mono);font-size:10px;letter-spacing:1.6px;
text-transform:uppercase;color:var(--deep);border:1px solid var(--line);background:rgba(0,0,0,.45);padding:3px 8px;border-radius:6px}}
.vbadge.live{{color:var(--gold-bright);border-color:var(--line2);background:rgba(201,151,58,.12)}}
.vbody{{padding:18px 20px 22px;display:flex;flex-direction:column;gap:6px}}
.vnum{{font-family:var(--mono);font-size:11px;letter-spacing:2px;color:var(--gold)}}
.vcard h3{{font-family:var(--serif);font-size:22px;font-weight:600;line-height:1.2}}
.vcard p{{color:var(--mute);font-size:14px}}

/* come-ready checklist */
.prep{{max-width:760px;margin:0 auto;background:linear-gradient(150deg,rgba(201,151,58,.1),rgba(0,0,0,.4));
border:1px solid var(--line2);border-radius:18px;padding:30px 36px}}
@media(max-width:600px){{.prep{{padding:24px 20px}}}}
.expect{{list-style:none}}
.expect li{{display:flex;gap:16px;align-items:flex-start;padding:15px 0;border-bottom:1px solid var(--line)}}
.expect li:last-child{{border-bottom:none;padding-bottom:0}}
.expect li div{{display:flex;flex-direction:column}}
.expect b{{color:var(--text);font-size:16px}}
.expect span{{color:var(--mute);font-size:14.5px}}
.cicon{{font-size:22px;color:var(--gold);flex:0 0 auto;margin-top:3px}}

/* confirm CTA */
.cta{{max-width:760px;margin:0 auto;text-align:center;background:linear-gradient(150deg,rgba(201,151,58,.14),rgba(0,0,0,.45));
border:1px solid var(--line2);border-radius:18px;padding:38px 36px}}
@media(max-width:600px){{.cta{{padding:28px 20px}}}}
.cta h2{{margin-bottom:10px}}
.cta p{{color:var(--mute);max-width:48ch;margin:0 auto 24px}}
.btn{{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(90deg,var(--gold-deep),var(--gold));
color:#0A0A0C;font-weight:700;font-size:16px;text-decoration:none;padding:15px 30px;border-radius:999px;
box-shadow:0 12px 34px rgba(201,151,58,.28);transition:.18s}}
.btn:hover{{transform:translateY(-2px);box-shadow:0 16px 40px rgba(201,151,58,.36)}}
.btn iconify-icon{{font-size:20px}}
.ctanum{{font-family:var(--mono);font-size:13px;letter-spacing:1px;color:var(--gold-bright);margin-top:18px}}
.ctanote{{font-size:13px;color:var(--deep);max-width:46ch;margin:12px auto 0}}

.shot{{background:linear-gradient(150deg,rgba(201,151,58,.06),rgba(0,0,0,.3));border:1px solid var(--line);border-radius:16px;padding:14px}}
.shot img{{width:100%;border-radius:10px;display:block;background:#fff}}
figcaption{{display:flex;flex-direction:column;gap:2px;padding:14px 6px 4px}}
figcaption b{{font-family:var(--serif);font-size:24px;color:var(--gold-bright);font-weight:700}}
figcaption span{{color:var(--mute);font-size:14px}}
.demo{{display:flex;flex-direction:column;background:linear-gradient(150deg,rgba(201,151,58,.06),rgba(0,0,0,.3));border:1px solid var(--line);border-radius:16px;overflow:hidden;text-decoration:none;transition:.18s;color:inherit}}
.demo:hover{{border-color:var(--line2);transform:translateY(-3px)}}
.demo-thumb{{aspect-ratio:16/10;overflow:hidden;border-bottom:1px solid var(--line);background:#fff}}
.demo-thumb img{{width:100%;height:100%;object-fit:cover;object-position:top;display:block}}
.demo-body{{padding:20px 22px}}
.demo h3{{font-family:var(--serif);font-size:23px;font-weight:600;margin-bottom:6px}}
.demo p{{color:var(--mute);font-size:14.5px;margin-bottom:14px}}
.demo-tag{{display:inline-block;font-family:var(--mono);font-size:10.5px;letter-spacing:2px;color:var(--gold);background:rgba(201,151,58,.12);border:1px solid var(--line);padding:3px 9px;border-radius:6px;margin-bottom:10px}}
.demo-link{{color:var(--gold-bright);font-weight:700;font-size:14.5px}}
.foot{{border-top:1px solid var(--line);padding:40px 0 70px;text-align:center;font-family:var(--mono);font-size:11px;letter-spacing:1px;color:var(--deep)}}
.foot .note{{color:var(--deep);font-size:12px;max-width:60ch;margin:0 auto 18px;font-family:var(--sans);letter-spacing:0;line-height:1.5}}
</style>
<script src="https://code.iconify.design/iconify-icon/2.1.0/iconify-icon.min.js"></script>
<div class="topbar"></div>
<div class="wrap">

  <div class="hero">
    <div class="logo"><b>AG1</b> Consulting</div>
    <div class="chip">You're booked</div>
    <h1>Your call is <em>confirmed.</em></h1>
    <p class="lede">Watch the quick video below so you know what to expect. Everything you would
    normally have to ask me on the call is answered on this page, so you can turn up already knowing.</p>
  </div>

  <section>
    <div class="eye" style="text-align:center">// Watch this first</div>
    <div style="max-width:820px;margin:0 auto;border-radius:18px;overflow:hidden;border:1px solid var(--line2)">
      <div style="position:relative;padding-bottom:56.25%;height:0">
        <iframe src="https://www.loom.com/embed/{LOOM_MAIN}?hideEmbedTopBar=true&amp;hide_owner=true&amp;hide_share=true&amp;hide_title=true" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>
      </div>
    </div>
  </section>

  <section>
    <div class="eye" style="text-align:center">// Your questions, answered before the call</div>
    <h2>The things you are <em>already thinking.</em></h2>
    <p class="sub">Short answers to what nearly every owner asks us. Watch the ones that apply to you,
    then hold me to them on the call.</p>
    <div class="vgrid">
{render_videos()}
    </div>
  </section>

  <section>
    <div class="eye" style="text-align:center">// Before we talk</div>
    <h2>Come <em>ready.</em></h2>
    <p class="sub">Six things that make the call worth your time.</p>
    <div class="prep">
      <ul class="expect">
{render_checklist()}
      </ul>
    </div>
  </section>

  <section>
    <div class="cta">
      <div class="eye">// One last thing</div>
      <h2>Confirm your <em>call.</em></h2>
      <p>You will have had a text from me. Reply <b>YES</b> to it and I will know you are coming,
      which means I will do the prep work on your business before we speak rather than after.</p>
      <a class="btn" href="sms:{SMS_TEL}?&amp;body=YES">
        <iconify-icon icon="mdi:message-reply-text-outline"></iconify-icon>
        Text YES to confirm
      </a>
      <div class="ctanum">{SMS_NUMBER}</div>
      <p class="ctanote">If something has come up and the time no longer works, text me and we will
      move it. I would rather move it than have you sat in a van missing it.</p>
    </div>
  </section>

  <section>
    <h2>What we've done for <em>other businesses.</em></h2>
    <p class="sub">Pulled straight from our clients' dashboards. This is the revenue our marketing has actually driven.</p>
    <div class="grid">
{render_proof()}
    </div>
  </section>

  <section>
    <h2>Here's the kind of <em>work you'll get.</em></h2>
    <p class="sub">Before we pitch you anything, we build you a website and a full audit. Here are two of each.</p>
    <div class="grid">
{render_demos()}
    </div>
  </section>

  <div class="foot">
    <p class="note">These are from clients and brands we've run marketing for across ecommerce, info and local business. Every screenshot is pulled straight from the platform. Results depend on your market, offer and spend.</p>
    &copy; AG1 Consulting Ltd &middot; See you on the call
  </div>

</div>
"""

if __name__ == "__main__":
    assert "—" not in HTML and "–" not in HTML, "dash policy: hyphens only"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"wrote {OUT} ({len(HTML)/1024/1024:.2f} MB)")
    print(f"breakout cards: {len(BREAKOUT_VIDEOS)} "
          f"({sum(1 for v in BREAKOUT_VIDEOS if v['loom'])} filmed, "
          f"{sum(1 for v in BREAKOUT_VIDEOS if not v['loom'])} placeholder)")
