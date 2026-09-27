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
SMS_NUMBER = "+44 7846 715676"          # UK, already wired into the confirm CTA
SMS_TEL = "+447846715676"
US_NUMBER = "+1 786 396 6358"           # US
US_TEL = "+17863966358"

# ---------------------------------------------------------------- breakout videos
# One card per objection, ranked as they appeared in the recorded sales calls.
# Titled as the prospect would ask it. loom=None renders a "being filmed" placeholder.
# 2026-09-27: refilmed with a proper microphone, and five more questions added, taking the set
# from 6 cards to 11. Every "loom" and "thumb" below was resolved through Loom's own oEmbed
# endpoint on that date, not typed from a share link:
#   * the thumb hash is NOT derivable from the share id. Omit or guess it and the card renders
#     black, which is the exact failure the page had on 2026-09-21.
#   * oEmbed also returns the clip's OWN title, which is the only way to catch a mislabelled id
#     before a prospect sees it. It caught two things: the source list labelled the "What we DO"
#     retake as Pt.1 when Loom (and the original it replaces) both call it Pt.2, and it confirmed
#     all 11 ids resolve publicly rather than being unlisted.
# The five originals these replaced: 5621049b / 06916a2c / c147de96 / 95eaf5e7 / 073a8997.
# "Why should I trust you?" is the ONE clip still on its original take - a retake was listed for
# it with no URL, so there was nothing to swap in. Replace it when that clip exists.
BREAKOUT_VIDEOS = [
    {
        "icon": "mdi:fire-alert",
        "q": "I have been burned by an agency before (part 1)",
        "teaser": "What we do not do, and why the lead-selling model produces the horror stories.",
        "loom": "b7fd29dfdcaf4accbc7b53c75cc610a8",
        "thumb": "b7fd29dfdcaf4accbc7b53c75cc610a8-f7d929ab36d26e4c",
    },
    {
        "icon": "mdi:shield-check-outline",
        "q": "I have been burned by an agency before (part 2)",
        "teaser": "What we actually do instead, and how you hold us to it.",
        "loom": "d7d7583c39fc4a57b0d818750f56aca4",
        "thumb": "d7d7583c39fc4a57b0d818750f56aca4-c1edec74636ae03e",
    },
    {
        "icon": "mdi:target",
        "q": "What is the Sniper Acquisition Method?",
        "teaser": "The system itself, in plain terms, and why it is built the way it is.",
        "loom": "c310ed1a74b1462aac1b58701c9fb156",
        "thumb": "c310ed1a74b1462aac1b58701c9fb156-0d817e849b69bcf8",
    },
    {
        "icon": "mdi:filter-check-outline",
        "q": "How do you make sure the appointments are qualified?",
        "teaser": "Where the qualifying happens, and why it happens before your phone ever rings.",
        "loom": "1d534f3ee36d4484ad9b802111d4e26c",
        "thumb": "1d534f3ee36d4484ad9b802111d4e26c-02f3b0b5c5422862",
    },
    {
        "icon": "mdi:lock-outline",
        "q": "Are the leads exclusive to me?",
        "teaser": "Yours alone. How that differs from the directories, and what it means in writing.",
        "loom": "8e73fe4fc8da474b91427dd8d681276e",
        "thumb": "8e73fe4fc8da474b91427dd8d681276e-4bf4b7490c58f288",
    },
    {
        "icon": "mdi:account-tie-outline",
        "q": "Why should I trust you?",
        "teaser": "You should not, not yet. Here are the things you can go and check instead.",
        "loom": "8fccfbf978804dc8a36821e9c5a8a759",
        "thumb": "8fccfbf978804dc8a36821e9c5a8a759-4a9ac0f24bd82bfe",
    },
    {
        "icon": "mdi:handshake-outline",
        "q": "What is a growth partner, and how do you work with clients?",
        "teaser": "What the arrangement actually is, and what working together looks like week to week.",
        "loom": "946424424f5d4d798ddb11275f0a7395",
        "thumb": "946424424f5d4d798ddb11275f0a7395-e531044351b3a25a",
    },
    {
        "icon": "mdi:account-hard-hat-outline",
        "q": "Why not just hire an in-house marketer?",
        "teaser": "What that route really costs you, and where it tends to come unstuck.",
        "loom": "3a9ab4bcca9648d285005acd68308701",
        "thumb": "3a9ab4bcca9648d285005acd68308701-d869b4a2bd23cbc6",
    },
    {
        "icon": "mdi:scale-balance",
        "q": "Cost per lead, or cost per QUALIFIED lead?",
        "teaser": "Why the cheaper number is usually the one that ends up costing you more.",
        "loom": "4d543cb5b7134fa4acb624518dba8332",
        "thumb": "4d543cb5b7134fa4acb624518dba8332-ca6e7f1a0af208e7",
    },
    {
        "icon": "mdi:chart-line",
        "q": "How will I know if my campaign has a return?",
        "teaser": "What gets measured, and how you see it rather than take our word for it.",
        "loom": "3b4fd95599e64d85b5e2e6481f16d7c9",
        "thumb": "3b4fd95599e64d85b5e2e6481f16d7c9-42987b361c70a602",
    },
    {
        "icon": "mdi:trending-up",
        "q": "What results can you expect?",
        "teaser": "What is realistic in your market, and what we will not promise you.",
        "loom": "3b7e795913484c609a5e49ac4db00bdb",
        "thumb": "3b7e795913484c609a5e49ac4db00bdb-fab0d65cbefcc51d",
    },
]

# Filmed later, kept so the topics are not lost. Move an entry up into
# BREAKOUT_VIDEOS with its loom id once the clip exists.
UNFILMED_TOPICS = [
    {"icon": "mdi:cash-multiple", "q": "What is this going to cost me?"},
    {"icon": "mdi:timer-sand", "q": "How long until I see anything?"},
    {"icon": "mdi:clipboard-check-outline", "q": "What do I actually have to do?"},
    {"icon": "mdi:calendar-clock-outline", "q": "I am already flat out, I cannot take more on"},
    {"icon": "mdi:calculator-variant-outline", "q": "Will this actually work at my margin?"},
    {"icon": "mdi:gesture-tap-button", "q": "I am not technical, will I be able to use it?"},
    {"icon": "mdi:vector-difference", "q": "What makes you different from the last lot?"},
    {"icon": "mdi:file-document-outline", "q": "Do you lock me into a contract?"},
    {"icon": "mdi:exit-run", "q": "What happens if I stop working with you?"},
    # "Why not just hire someone in-house?" moved up into BREAKOUT_VIDEOS on 2026-09-27 - filmed.
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
    """Real Loom thumbnail as a poster, iframe created only on click.

    Why a facade and not six live iframes: six Loom players initialising at
    once starve each other. Proved by screenshotting the live page twice on
    2026-09-21 - a DIFFERENT video rendered each run and the rest stayed
    black. Non-deterministic, which is why it read as random.

    The poster is Loom's own thumbnail from its oEmbed endpoint, with .gif
    swapped for .jpg: 44-101KB instead of 1.4-3.4MB."""
    out = []
    for v in BREAKOUT_VIDEOS:
        if not v.get("loom"):
            continue
        thumb = (f"https://cdn.loom.com/sessions/thumbnails/{v['thumb']}.jpg"
                 if v.get("thumb") else "")
        out.append(f"""    <div class="vitem">
      <h3 class="vq">{v['q']}</h3>
      <a class="vembed" href="https://www.loom.com/share/{v['loom']}"
         target="_blank" rel="noopener"
         data-loom="{v['loom']}" aria-label="Play: {v['q']}">
        <img src="{thumb}" alt="" loading="lazy" decoding="async">
        <span class="vplaybtn" aria-hidden="true"></span>
      </a>
      <a class="vlink" href="https://www.loom.com/share/{v['loom']}"
         target="_blank" rel="noopener">Not playing? Watch it on Loom &rarr;</a>
    </div>""")
    return chr(10).join(out)


PLAYER_JS = """<script>
document.querySelectorAll('a.vembed[data-loom]').forEach(function(a){
  a.addEventListener('click', function(e){
    if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
    e.preventDefault();
    if (a.dataset.playing) return;
    a.dataset.playing = '1';
    a.innerHTML = '<iframe src="https://www.loom.com/embed/' + a.dataset.loom +
      '?autoplay=1" frameborder="0" allow="autoplay; fullscreen"' +
      ' allowfullscreen></iframe>';
  });
});
</script>"""


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


STYLE = f"""<style>
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

/* breakout videos: question above, poster below, two columns */
.vgrid{{display:grid;grid-template-columns:repeat(2,1fr);gap:34px 30px}}
@media(max-width:760px){{.vgrid{{grid-template-columns:1fr;gap:26px}}}}
.vitem{{display:flex;flex-direction:column;gap:12px}}
.vq{{font-family:var(--sans);font-size:15px;font-weight:700;letter-spacing:.6px;
text-transform:uppercase;line-height:1.3;color:var(--gold-bright)}}
.vembed{{position:relative;display:block;width:100%;aspect-ratio:16/9;min-height:190px;
overflow:hidden;border-radius:12px;border:1px solid var(--line);background:#000;
cursor:pointer;transition:.18s}}
.vembed:hover{{border-color:var(--line2);transform:translateY(-2px)}}
.vembed img{{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;display:block}}
.vembed iframe{{position:absolute;top:0;left:0;width:100%;height:100%;border:0;display:block}}
.vplaybtn{{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:62px;height:62px;
border-radius:50%;background:rgba(0,0,0,.55);border:2px solid #fff;display:flex;
align-items:center;justify-content:center;transition:.18s}}
.vembed:hover .vplaybtn{{background:var(--gold);border-color:var(--gold)}}
.vplaybtn:after{{content:"";border-left:19px solid #fff;border-top:12px solid transparent;
border-bottom:12px solid transparent;margin-left:6px}}
.vembed:hover .vplaybtn:after{{border-left-color:#000}}
.ctabtns{{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}}
@media(max-width:520px){{.ctabtns{{flex-direction:column;align-items:stretch}}}}
.vlink{{font-family:var(--sans);font-size:13px;color:var(--mute);text-decoration:none;
border-bottom:1px solid var(--line2);align-self:flex-start;padding-bottom:1px;transition:.15s}}
.vlink:hover{{color:var(--gold-bright);border-color:var(--gold)}}

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
</style>"""

HTML = STYLE + f"""
<script src="https://code.iconify.design/iconify-icon/2.1.0/iconify-icon.min.js"></script>
<div class="topbar"></div>
<div class="wrap">

  <div class="hero">
    <div class="logo"><b>AG1</b> Consulting</div>
    <div class="chip">Your Zoom call has been scheduled</div>
    <h1>Watch these quick videos to see how we generate <em>qualified appointments</em> using our
    Sniper Acquisition Method.</h1>
    <p class="lede">Everything you would normally have to ask me on the call is answered on this page,
    so you can turn up already knowing.</p>
    <p class="lede" style="margin-top:14px"><b>Important:</b> confirm you are coming, either way is
    fine. If you had the calendar invite by email, hit <b>Yes</b> on it. If you had my text, reply
    <b>YES</b> to that. Once I know you are coming I will do the prep work on your business before
    we speak rather than after.</p>
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
      <div class="ctabtns">
        <a class="btn" href="sms:{SMS_TEL}?&amp;body=YES">
          <iconify-icon icon="mdi:message-reply-text-outline"></iconify-icon>
          Text YES &middot; UK {SMS_NUMBER}
        </a>
        <a class="btn" href="sms:{US_TEL}?&amp;body=YES">
          <iconify-icon icon="mdi:message-reply-text-outline"></iconify-icon>
          Text YES &middot; US {US_NUMBER}
        </a>
      </div>
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
{PLAYER_JS}
"""

# ---------------------------------------------------------------- questions page
QUESTIONS_OUT = os.path.join(os.path.dirname(HERE), "questions", "index.html")

QUESTIONS_HTML = STYLE + f"""
<script src="https://code.iconify.design/iconify-icon/2.1.0/iconify-icon.min.js"></script>
<div class="topbar"></div>
<div class="wrap">

  <div class="hero">
    <div class="logo"><b>AG1</b> Consulting</div>
    <div class="chip">Before we speak</div>
    <h1>Get your questions <em>answered.</em></h1>
    <p class="lede">Short answers to what nearly every roofing owner asks us, straight from me
    rather than from a brochure. Watch the ones that apply to you, then hold me to them on the call.</p>
  </div>

  <section>
    <div class="vgrid">
{render_videos()}
    </div>
  </section>

  <section>
    <h2>What we've done for <em>other businesses.</em></h2>
    <p class="sub">Pulled straight from our clients' dashboards. This is the revenue our marketing
    has actually driven.</p>
    <div class="grid">
{render_proof()}
    </div>
    <p class="ctanote" style="text-align:center;margin-top:18px">Every screenshot is pulled straight
    from the platform. Results depend on your market, offer and spend.</p>
  </section>

  <section>
    <div class="cta">
      <div class="eye">// Still on your mind</div>
      <h2>Ask me the <em>rest.</em></h2>
      <p>If the thing you are wondering about is not on this page, text it to me before the call
      and I will answer it properly rather than off the cuff.</p>
      <div class="ctabtns">
        <a class="btn" href="sms:{SMS_TEL}">
          <iconify-icon icon="mdi:message-text-outline"></iconify-icon>
          Text UK {SMS_NUMBER}
        </a>
        <a class="btn" href="sms:{US_TEL}">
          <iconify-icon icon="mdi:message-text-outline"></iconify-icon>
          Text US {US_NUMBER}
        </a>
      </div>
    </div>
  </section>

  <div class="foot">
    &copy; AG1 Consulting Ltd &middot; See you on the call
  </div>

</div>
{PLAYER_JS}
"""


# ---------------------------------------------------------------- temporary link-out page
# /watch/ - same thumbnails, but every card OPENS LOOM IN A NEW TAB instead of
# embedding. No PLAYER_JS, so the anchor's href is followed normally. Built
# 2026-09-21 because the in-page embeds were not playing and the cause was not
# yet established; this sidesteps the embed path entirely.
WATCH_OUT = os.path.join(os.path.dirname(HERE), "watch", "index.html")

WATCH_HTML = STYLE + f"""
<div class="topbar"></div>
<div class="wrap">

  <div class="hero">
    <div class="logo"><b>AG1</b> Consulting</div>
    <div class="chip">Before we speak</div>
    <h1>Get your questions <em>answered.</em></h1>
    <p class="lede">Short answers to what nearly every roofing owner asks us, straight from me
    rather than from a brochure. Click any one to watch it. Then hold me to them on the call.</p>
  </div>

  <section>
    <div class="vgrid">
{render_videos()}
    </div>
  </section>

  <section>
    <div class="cta">
      <div class="eye">// Still on your mind</div>
      <h2>Ask me the <em>rest.</em></h2>
      <p>If the thing you are wondering about is not on this page, text it to me before the call
      and I will answer it properly rather than off the cuff.</p>
      <div class="ctabtns">
        <a class="btn" href="sms:{SMS_TEL}">Text UK {SMS_NUMBER}</a>
        <a class="btn" href="sms:{US_TEL}">Text US {US_NUMBER}</a>
      </div>
    </div>
  </section>

  <div class="foot">
    &copy; AG1 Consulting Ltd &middot; See you on the call
  </div>

</div>
"""


def check_videos():
    """Fail the build rather than ship a card that cannot render.

    Each of these has already happened once. A thumb that does not belong to its own share id
    renders a poster of the WRONG video, or a black box if the hash is stale - and the page looks
    fine in the source, so it is only visible to the prospect. The same id twice means a question
    was pasted over instead of added, which silently loses a clip.
    """
    ids = [v["loom"] for v in BREAKOUT_VIDEOS if v.get("loom")]
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, "same Loom id on two cards: %s" % ", ".join(sorted(dupes))
    for v in BREAKOUT_VIDEOS:
        if not v.get("loom"):
            continue
        t = v.get("thumb") or ""
        assert t, "%r has no thumb - the card would render black" % v["q"]
        assert t.startswith(v["loom"] + "-"), (
            "%r: thumb %r is not this video's (expected it to start with %s-). Re-resolve it "
            "through https://www.loom.com/v1/oembed?url=https://www.loom.com/share/<id>"
            % (v["q"], t, v["loom"]))
    qs = [v["q"] for v in BREAKOUT_VIDEOS]
    assert len(set(qs)) == len(qs), "two cards ask the same question"


if __name__ == "__main__":
    check_videos()
    assert "—" not in HTML and "–" not in HTML, "dash policy: hyphens only"
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(HTML)
    print(f"wrote {OUT} ({len(HTML)/1024/1024:.2f} MB)")
    os.makedirs(os.path.dirname(QUESTIONS_OUT), exist_ok=True)
    assert "—" not in QUESTIONS_HTML and "–" not in QUESTIONS_HTML, "dash policy: hyphens only"
    with open(QUESTIONS_OUT, "w", encoding="utf-8") as f:
        f.write(QUESTIONS_HTML)
    print(f"wrote {QUESTIONS_OUT} ({len(QUESTIONS_HTML)/1024:.0f} KB)")
    os.makedirs(os.path.dirname(WATCH_OUT), exist_ok=True)
    assert "—" not in WATCH_HTML and "–" not in WATCH_HTML, "dash policy: hyphens only"
    with open(WATCH_OUT, "w", encoding="utf-8") as f:
        f.write(WATCH_HTML)
    print(f"wrote {WATCH_OUT} ({len(WATCH_HTML)/1024:.0f} KB)")
    print(f"breakout cards: {len(BREAKOUT_VIDEOS)} "
          f"({sum(1 for v in BREAKOUT_VIDEOS if v['loom'])} filmed, "
          f"{sum(1 for v in BREAKOUT_VIDEOS if not v['loom'])} placeholder)")