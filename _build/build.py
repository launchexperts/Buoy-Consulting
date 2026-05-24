"""
Page generator for buoyconsultancy.com.au

Generates the 15 inner pages from a shared layout. Run from anywhere:
    python _build/build.py

Edit the PAGE content blocks below to update copy, then re-run to regenerate.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Bump this whenever styles.css changes — appended as ?v=N to <link> hrefs
# so browsers don't serve a stale stylesheet.
CSS_VERSION = "28"

# ============================================================
# CSS additions for inner pages — appended to styles.css if missing
# ============================================================
INNER_CSS_MARKER = "/* === INNER-PAGE STYLES ==="
INNER_CSS = """
/* === INNER-PAGE STYLES ============================================== */
.page-hero {
  padding: clamp(3.5rem, 6vw, 5.5rem) 0 clamp(2rem, 4vw, 3rem);
}
.page-hero .eyebrow { margin-bottom: 1.25rem; }
.page-hero h1 {
  font-size: clamp(2.25rem, 4.6vw, 4rem);
  max-width: 18ch;
  margin-bottom: 1.5rem;
}
.page-hero .lead {
  font-size: var(--fs-lead);
  color: var(--gray-700);
  max-width: 60ch;
  line-height: 1.6;
}
.page-hero.center { text-align: center; }
.page-hero.center h1, .page-hero.center .lead { margin-inline: auto; }

.page-hero.with-visual .hero-grid {
  display: grid;
  grid-template-columns: 1.05fr 1fr;
  gap: clamp(2rem, 5vw, 5rem);
  align-items: center;
}
.page-hero.with-visual .hero-text { max-width: 580px; }
.page-hero.with-visual .hero-visual-card {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: clamp(20px, 2.5vw, 32px);
  overflow: hidden;
  background: var(--orange-100);
  box-shadow: var(--shadow-float);
}
.page-hero.with-visual .hero-visual-card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.page-hero.with-visual .hero-visual-card .badge {
  position: absolute;
  bottom: 1.25rem;
  left: 1.25rem;
  background: var(--ink-900);
  color: var(--white);
  padding: 0.55rem 1rem;
  border-radius: var(--r-pill);
  font-size: 0.75rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  box-shadow: var(--shadow-soft);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
}
.page-hero.with-visual .hero-visual-card .badge .pulse {
  display: inline-block;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--orange-500);
  animation: pulse 2s ease-in-out infinite;
}
.page-hero.with-visual .hero-visual-card .blob-accent {
  position: absolute;
  width: 140px; height: 140px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.55;
  bottom: -50px; right: -50px;
  z-index: -1;
}
@media (max-width: 900px) {
  .page-hero.with-visual .hero-grid { grid-template-columns: 1fr; }
  .page-hero.with-visual .hero-visual-card { max-width: 540px; margin-inline: auto; }
}

/* Section with side photo (alternating direction) */
.section-photo-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(2rem, 5vw, 4rem);
  align-items: center;
}
.section-photo-split.reverse { direction: rtl; }
.section-photo-split.reverse > * { direction: ltr; }
.section-photo-split .photo {
  position: relative;
  aspect-ratio: 4 / 3;
  border-radius: clamp(20px, 2vw, 28px);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
}
.section-photo-split .photo img {
  width: 100%; height: 100%; object-fit: cover;
}
@media (max-width: 800px) {
  .section-photo-split, .section-photo-split.reverse { grid-template-columns: 1fr; direction: ltr; }
}

.section { padding-block: clamp(3rem, 5vw, 5rem); }
.section.tight { padding-block: clamp(2rem, 3.5vw, 3rem); }
.section h2 {
  font-size: clamp(1.75rem, 3vw, 2.5rem);
  margin-bottom: 1.5rem;
  max-width: 22ch;
}
.section .lead {
  font-size: var(--fs-lead);
  color: var(--gray-700);
  max-width: 60ch;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}
.section p {
  color: var(--gray-700);
  line-height: 1.7;
  margin-bottom: 1rem;
  max-width: 62ch;
}
.section.warm-bg {
  background: var(--orange-50);
  border-radius: 32px;
  margin-inline: var(--gutter);
}
.section.cream-bg {
  background: var(--cream);
}

.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: clamp(2rem, 4vw, 4rem);
  align-items: start;
}
.two-col.aside { grid-template-columns: 1.2fr 1fr; }
@media (max-width: 800px) {
  .two-col, .two-col.aside { grid-template-columns: 1fr; }
}

.deliverables, .checklist {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  margin: 2rem 0;
}
.deliverables li, .checklist li {
  position: relative;
  padding-left: 2.25rem;
  color: var(--gray-700);
  line-height: 1.55;
}
.deliverables li::before, .checklist li::before {
  content: "";
  position: absolute;
  left: 0; top: 6px;
  width: 18px; height: 18px;
  border-radius: 50%;
  background: var(--orange-100);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23E85D1F' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 11px;
}
.deliverables li strong, .checklist li strong {
  color: var(--ink);
  display: block;
  margin-bottom: 0.15rem;
  font-weight: 700;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  margin-top: 2rem;
}
.feature-card {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: 1.6rem;
  transition: transform 250ms, border-color 200ms, box-shadow 250ms;
}
.feature-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-300);
  box-shadow: var(--shadow-soft);
}
.feature-card .num {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.85rem;
  color: var(--orange-700);
  letter-spacing: 0.06em;
  text-transform: uppercase;
  margin-bottom: 0.65rem;
}
.feature-card h3 {
  font-size: 1.1rem;
  margin-bottom: 0.5rem;
}
.feature-card p {
  font-size: 0.93rem;
  color: var(--gray-700);
  line-height: 1.55;
  margin: 0;
}

.sub-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-top: 2.5rem;
}
.sub-card {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: 1.75rem;
  display: flex; flex-direction: column; gap: 0.85rem;
  transition: transform 250ms, border-color 200ms, box-shadow 250ms;
  min-height: 200px;
}
.sub-card:hover {
  transform: translateY(-6px);
  border-color: var(--orange-300);
  box-shadow: var(--shadow-soft);
}
.sub-card .icon {
  width: 44px; height: 44px;
  border-radius: 12px;
  background: var(--orange-100);
  color: var(--orange-700);
  display: grid; place-items: center;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: -0.02em;
}
.sub-card h3 { font-size: 1.15rem; }
.sub-card p {
  font-size: 0.92rem;
  color: var(--gray-700);
  line-height: 1.55;
  flex: 1;
  margin: 0;
}
.sub-card .more {
  display: inline-flex; align-items: center; gap: 0.4rem;
  font-size: 0.9rem; color: var(--orange-700); font-weight: 500;
}
.sub-card:hover .more { gap: 0.6rem; }

.same-day-banner {
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  padding: 0.5rem 1rem;
  background: var(--orange-100);
  color: var(--orange-700);
  border-radius: var(--r-pill);
  font-size: 0.85rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}
.same-day-banner .pulse {
  width: 8px; height: 8px;
  border-radius: 50%;
  background: var(--orange-500);
  animation: pulse 2s ease-in-out infinite;
}

.outcomes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin: 2rem 0;
}
.outcomes .o {
  padding: 1.25rem;
  background: var(--orange-50);
  border-radius: var(--r-card);
  border-left: 3px solid var(--orange-500);
}
.outcomes .o .num {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.85rem;
  color: var(--ink);
  letter-spacing: -0.02em;
  display: block;
  margin-bottom: 0.25rem;
}
.outcomes .o .lbl {
  font-size: 0.85rem;
  color: var(--gray-700);
  line-height: 1.4;
}

.inline-cta {
  background: linear-gradient(135deg, var(--ink-900) 0%, var(--ink-800) 100%);
  color: var(--white);
  border-radius: 28px;
  padding: clamp(2.5rem, 5vw, 4rem);
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: 2rem;
  align-items: center;
  position: relative;
  overflow: hidden;
}
.inline-cta::before {
  content: "";
  position: absolute;
  width: 320px; height: 320px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--orange-500) 0%, transparent 70%);
  opacity: 0.3;
  top: -100px; right: -80px;
}
.inline-cta h2 { color: var(--white); margin-bottom: 0.75rem; }
.inline-cta p {
  color: rgba(255,255,255,0.75);
  margin-bottom: 0;
}
.inline-cta .cta-actions {
  display: flex; gap: 0.75rem; flex-wrap: wrap;
  justify-content: flex-end;
}
.inline-cta .btn-primary {
  background: var(--orange-500); color: var(--white);
  padding: 1.05rem 1.75rem; font-weight: 600;
}
.inline-cta .btn-primary:hover { background: var(--orange-700); }
.inline-cta .btn-ghost {
  background: transparent; color: var(--white);
  border: 1px solid rgba(255,255,255,0.25);
}
.inline-cta .btn-ghost:hover { border-color: var(--white); background: rgba(255,255,255,0.08); }
@media (max-width: 800px) {
  .inline-cta { grid-template-columns: 1fr; padding: 2.5rem; }
  .inline-cta .cta-actions { justify-content: flex-start; }
}

/* Active nav state */
.nav-links > li > a.active { color: var(--orange-700); }
.nav-links > li.has-dropdown.active > a { color: var(--orange-700); }
/* Keep Services parent highlighted while the dropdown is hovered/focused */
.nav-links > li.has-dropdown:hover > a,
.nav-links > li.has-dropdown:focus-within > a { color: var(--orange-700); }

/* === Dark sections (testimonial, stat ticker, etc.) === */
.section.dark {
  background: linear-gradient(135deg, var(--ink-900) 0%, var(--ink-800) 60%, var(--ink-700) 100%);
  color: var(--white);
  border-radius: 32px;
  margin-inline: var(--gutter);
  position: relative;
  overflow: hidden;
}
.section.dark::before {
  content: "";
  position: absolute;
  width: 480px; height: 480px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--orange-500) 0%, transparent 65%);
  opacity: 0.28;
  top: -200px; right: -120px;
  pointer-events: none;
  z-index: 0;
}
.section.dark::after {
  content: "";
  position: absolute;
  width: 320px; height: 320px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--orange-300) 0%, transparent 60%);
  opacity: 0.18;
  bottom: -140px; left: -80px;
  pointer-events: none;
  z-index: 0;
}
.section.dark > .wrap { position: relative; z-index: 1; }
.section.dark h2, .section.dark h3, .section.dark h4 { color: var(--white); }
.section.dark p { color: rgba(255, 255, 255, 0.78); }
.section.dark .lead { color: rgba(255, 255, 255, 0.75); }
.section.dark .eyebrow { color: var(--orange-300); }
.section.dark .eyebrow::before { background: var(--orange-400); }

/* === Testimonial quote === */
.quote-block {
  max-width: 880px;
  margin: 0 auto;
  text-align: center;
  position: relative;
  padding: 1rem 0;
}
.quote-block::before {
  content: "\"";
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(7rem, 14vw, 11rem);
  color: var(--orange-500);
  opacity: 0.35;
  position: absolute;
  top: -2.5rem;
  left: 50%;
  transform: translateX(-50%);
  line-height: 1;
  pointer-events: none;
}
.quote-text {
  font-family: var(--font-display);
  font-weight: 500;
  font-size: clamp(1.35rem, 2.4vw, 1.85rem);
  line-height: 1.45;
  letter-spacing: -0.01em;
  color: var(--white) !important;
  margin-bottom: 2rem;
  position: relative;
  z-index: 2;
}
.quote-text em {
  color: var(--orange-300);
  font-style: normal;
  font-weight: 700;
}
.quote-attr {
  display: inline-flex;
  align-items: center;
  gap: 0.85rem;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  padding: 0.6rem 1.1rem 0.6rem 0.6rem;
  border-radius: var(--r-pill);
}
.quote-attr .avatar {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--orange-300), var(--orange-500));
  display: grid; place-items: center;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.8rem;
  color: var(--white);
  letter-spacing: 0.04em;
}
.quote-attr .who {
  text-align: left;
  display: flex; flex-direction: column;
  line-height: 1.25;
}
.quote-attr .who strong {
  font-weight: 700;
  font-size: 0.9rem;
  color: var(--white) !important;
}
.quote-attr .who span {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.6);
}

/* === Stat ticker (homepage trust-strip cousin) === */
.stat-ticker {
  background: var(--ink-900);
  color: var(--white);
  padding: 1.5rem 0;
  overflow: hidden;
  border-radius: 0;
  margin-inline: calc(-1 * var(--gutter));
  position: relative;
}
.stat-ticker::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, var(--ink-900) 0%, transparent 8%, transparent 92%, var(--ink-900) 100%);
  pointer-events: none;
  z-index: 2;
}
.stat-ticker-track {
  display: flex;
  gap: 3.5rem;
  white-space: nowrap;
  animation: ticker 45s linear infinite;
  align-items: center;
}
.stat-ticker .item {
  display: inline-flex;
  align-items: baseline;
  gap: 0.6rem;
  font-family: var(--font-display);
}
.stat-ticker .item .num {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--orange-300);
  letter-spacing: -0.02em;
}
.stat-ticker .item .lbl {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.7);
  font-weight: 500;
  letter-spacing: 0.02em;
}
.stat-ticker .item::after {
  content: "✦";
  margin-left: 3rem;
  color: var(--orange-500);
  font-size: 0.8rem;
}

/* === Decorative section blob === */
.section.has-blob {
  position: relative;
  overflow: hidden;
}
.section.has-blob::before {
  content: "";
  position: absolute;
  width: 280px; height: 280px;
  border-radius: 50%;
  background: var(--orange-100);
  opacity: 0.55;
  pointer-events: none;
  z-index: 0;
}
.section.has-blob.blob-tr::before { top: -100px; right: -80px; }
.section.has-blob.blob-bl::before { bottom: -100px; left: -80px; background: var(--orange-300); opacity: 0.25; }
.section.has-blob > .wrap { position: relative; z-index: 1; }

/* === Team detail grid (team.html) === */
.team-detail {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-top: 2.5rem;
}
.team-detail .person {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: 1.75rem;
  display: flex; flex-direction: column; gap: 0.85rem;
  transition: transform 250ms, border-color 200ms, box-shadow 250ms;
}
.team-detail .person:hover {
  transform: translateY(-4px);
  border-color: var(--orange-300);
  box-shadow: var(--shadow-soft);
}
.team-detail .person .photo {
  width: 86px;
  aspect-ratio: 1 / 1;
  border-radius: 50%;
  overflow: hidden;
  background: linear-gradient(135deg, var(--orange-300), var(--orange-500));
}
.team-detail .person .photo img {
  width: 100%; height: 100%; object-fit: cover; display: block;
}
.team-detail .person .photo.photo-placeholder {
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--orange-400), var(--orange-700));
}
.team-detail .person .photo.photo-placeholder span {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 1.65rem;
  letter-spacing: 0.04em;
  color: var(--white);
}
.team-detail .person h3 {
  font-size: 1.15rem; margin: 0;
  letter-spacing: -0.01em;
}
.team-detail .person .role {
  font-size: 0.85rem;
  color: var(--orange-700);
  font-weight: 500;
  margin: 0;
}
.team-detail .person .bio {
  font-size: 0.92rem;
  color: var(--gray-700);
  line-height: 1.55;
  margin: 0;
  flex: 1;
}
/* LinkedIn / social pill on team-detail person cards */
.team-detail .person .person-social {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  align-self: flex-start;
  margin-top: 0.5rem;
  padding: 0.5rem 0.95rem 0.5rem 0.75rem;
  background: var(--orange-50);
  border: 1px solid var(--orange-100);
  border-radius: var(--r-pill);
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--orange-700);
  letter-spacing: 0.01em;
  transition: background 200ms, border-color 200ms, color 200ms, transform 200ms;
}
.team-detail .person .person-social:hover {
  background: var(--orange-500);
  border-color: var(--orange-500);
  color: var(--white);
  transform: translateY(-2px);
}

/* === FAQ accordion (process.html) === */
.faq {
  display: flex; flex-direction: column;
  gap: 0.75rem;
  max-width: 760px;
  margin-top: 2rem;
}
.faq details {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-tight);
  padding: 1.1rem 1.4rem;
  transition: border-color 200ms;
}
.faq details[open] { border-color: var(--orange-300); }
.faq summary {
  font-weight: 700;
  font-family: var(--font-display);
  cursor: pointer;
  color: var(--ink);
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}
.faq summary::-webkit-details-marker { display: none; }
.faq summary::after {
  content: "+";
  font-size: 1.5rem;
  color: var(--orange-500);
  font-weight: 700;
  line-height: 1;
  transition: transform 200ms;
}
.faq details[open] summary::after { content: "−"; }
.faq details p {
  margin-top: 0.85rem;
  color: var(--gray-700);
  line-height: 1.7;
  font-size: 0.95rem;
}

/* === Process timeline (process.html) === */
.process-timeline {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-top: 2.5rem;
}
.process-timeline .phase {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: 1.75rem 2rem;
  display: grid;
  grid-template-columns: 80px 1fr;
  gap: 1.5rem;
  transition: border-color 200ms, transform 250ms;
}
.process-timeline .phase:hover {
  border-color: var(--orange-300);
  transform: translateX(4px);
}
.process-timeline .phase .num {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 2.5rem;
  color: var(--orange-500);
  letter-spacing: -0.04em;
  line-height: 1;
}
.process-timeline .phase h3 {
  font-size: 1.3rem;
  margin-bottom: 0.4rem;
}
.process-timeline .phase .duration {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--orange-700);
  font-weight: 700;
  margin-bottom: 0.85rem;
}
.process-timeline .phase p {
  color: var(--gray-700);
  line-height: 1.65;
  margin: 0 0 0.5rem;
  font-size: 0.95rem;
}
@media (max-width: 600px) {
  .process-timeline .phase { grid-template-columns: 1fr; gap: 0.5rem; padding: 1.5rem; }
  .process-timeline .phase .num { font-size: 2rem; }
}

/* Contact form */
.contact-form {
  display: flex; flex-direction: column; gap: 1.25rem;
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: clamp(1.75rem, 3vw, 2.5rem);
  margin-top: 2rem;
}
.contact-form .field { display: flex; flex-direction: column; gap: 0.4rem; }
.contact-form label {
  font-size: 0.78rem; font-weight: 700;
  color: var(--ink); letter-spacing: 0.05em;
  text-transform: uppercase;
}
.contact-form input, .contact-form textarea, .contact-form select {
  padding: 0.85rem 1rem;
  border: 1px solid var(--gray-300);
  border-radius: var(--r-tight);
  font: inherit; color: var(--ink); background: var(--cream);
  transition: border-color 200ms, background 200ms;
}
.contact-form input:focus, .contact-form textarea:focus, .contact-form select:focus {
  outline: none; border-color: var(--orange-500); background: var(--white);
}
.contact-form textarea { min-height: 120px; resize: vertical; }
.contact-form button {
  background: var(--orange-500); color: var(--white);
  padding: 1rem 1.75rem;
  border-radius: var(--r-pill);
  font-weight: 600; font-size: 0.95rem;
  cursor: pointer;
  transition: background 200ms, transform 200ms;
  align-self: flex-start;
}
.contact-form button:hover { background: var(--orange-700); transform: translateY(-1px); }

.contact-aside {
  display: flex; flex-direction: column; gap: 1.5rem;
}
.contact-aside h3 { font-size: 1.1rem; }
.contact-aside .channel {
  display: flex; flex-direction: column; gap: 0.25rem;
}
.contact-aside .channel a {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.15rem;
  color: var(--ink);
}
.contact-aside .channel a:hover { color: var(--orange-700); }
.contact-aside .channel span {
  font-size: 0.85rem; color: var(--gray-500);
}

/* === Contact page — 3-up channels grid (on warm-bg-rich) === */
.contact-channels {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
@media (max-width: 900px) { .contact-channels { grid-template-columns: 1fr; max-width: 480px; margin-inline: auto; } }

.contact-channel-card {
  background: var(--white);
  border: 1px solid var(--orange-100);
  border-radius: var(--r-card);
  padding: 1.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  text-decoration: none;
  color: inherit;
  box-shadow: 0 10px 24px -14px rgba(14, 23, 41, 0.08);
  transition: transform 250ms ease, border-color 200ms, box-shadow 300ms;
}
.contact-channel-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-300);
  box-shadow: 0 24px 48px -20px rgba(14, 23, 41, 0.18);
}
.contact-channel-card .cc-icon {
  width: 52px; height: 52px;
  border-radius: 14px;
  background: var(--orange-100);
  color: var(--orange-700);
  display: grid; place-items: center;
  margin-bottom: 0.75rem;
  transition: background 250ms, color 250ms, transform 350ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.contact-channel-card:hover .cc-icon {
  background: var(--orange-500);
  color: var(--white);
  transform: scale(1.08) rotate(-6deg);
}
.contact-channel-card .cc-label {
  font-family: var(--font-body);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--orange-700);
}
.contact-channel-card .cc-handle {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.2rem;
  letter-spacing: -0.015em;
  color: var(--ink);
  word-break: break-word;
  line-height: 1.25;
}
.contact-channel-card .cc-meta {
  font-size: 0.85rem;
  color: var(--gray-500);
  line-height: 1.45;
  margin-top: 0.2rem;
}

/* === Contact page — 3-up "What happens next" cards === */
.next-steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
@media (max-width: 900px) { .next-steps-grid { grid-template-columns: 1fr; max-width: 480px; margin-inline: auto; } }

.next-step-card {
  background: var(--white);
  border: 1px solid var(--orange-100);
  border-radius: var(--r-card);
  padding: 1.85rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  position: relative;
  overflow: hidden;
  transition: transform 250ms ease, border-color 200ms, box-shadow 300ms;
  box-shadow: 0 6px 18px -10px rgba(14, 23, 41, 0.10);
}
.next-step-card:hover {
  transform: translateY(-4px);
  border-color: var(--orange-300);
  box-shadow: 0 24px 48px -20px rgba(14, 23, 41, 0.16);
}
.next-step-card .step-num {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 2.5rem;
  color: var(--orange-500);
  letter-spacing: -0.04em;
  line-height: 1;
  display: block;
  margin-bottom: 0.5rem;
}
.next-step-card h3 {
  font-size: 1.15rem;
  margin-bottom: 0.5rem;
  letter-spacing: -0.01em;
}
.next-step-card p {
  color: var(--gray-700);
  font-size: 0.92rem;
  line-height: 1.55;
  margin: 0;
}

/* === Page hero — atmospheric peach gradient (applies to every inner-page hero) === */
.page-hero {
  position: relative;
  overflow: hidden;
  background: linear-gradient(180deg, var(--orange-100) 0%, var(--orange-50) 45%, var(--cream) 100%);
}
.page-hero::before {
  content: "";
  position: absolute;
  width: 640px; height: 640px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.18;
  top: -260px; right: -200px;
  pointer-events: none;
  z-index: 0;
}
.page-hero.center::before {
  /* For centered heroes, soft blob more central rather than top-right */
  left: 50%;
  right: auto;
  transform: translateX(-50%);
  top: -340px;
  opacity: 0.14;
}
.page-hero > .wrap { position: relative; z-index: 1; }

/* Italic emphasis on page-hero H1 (matches homepage's italic Jobpac treatment) */
.page-hero h1 em {
  font-style: italic;
  font-weight: 700;
  color: var(--orange-500);
}

/* Hero floating card overlay */
.page-hero.with-visual .hero-visual-card-wrap { position: relative; }
.page-hero.with-visual .hero-float-card {
  position: absolute;
  bottom: -20px;
  left: -28px;
  background: var(--white);
  box-shadow: var(--shadow-float);
  border-radius: 14px;
  padding: 0.85rem 1.05rem;
  display: flex;
  align-items: center;
  gap: 0.75rem;
  z-index: 3;
  transform: rotate(-2deg);
  transition: transform 600ms cubic-bezier(0.4, 0, 0.2, 1);
  max-width: 240px;
}
.page-hero.with-visual .hero-visual-card-wrap:hover .hero-float-card {
  transform: rotate(0deg) translateY(-3px);
}
.page-hero.with-visual .hero-float-card .hf-icon {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: var(--orange-500);
  color: var(--white);
  display: grid; place-items: center;
  flex-shrink: 0;
}
.page-hero.with-visual .hero-float-card .hf-meta {
  display: flex;
  flex-direction: column;
  line-height: 1.2;
}
.page-hero.with-visual .hero-float-card .hf-meta b {
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: -0.01em;
  color: var(--ink);
}
.page-hero.with-visual .hero-float-card .hf-meta span {
  font-size: 0.72rem;
  color: var(--gray-500);
}
@media (max-width: 900px) {
  .page-hero.with-visual .hero-float-card { left: 8px; bottom: -14px; }
}

/* === Centered inner-page section head === */
.section-head {
  text-align: center;
  max-width: 720px;
  margin: 0 auto clamp(2.5rem, 4vw, 3.5rem);
}
.section-head .eyebrow { margin-bottom: 1.25rem; }
.section-head h2 { margin-bottom: 1rem; max-width: none; }
.section-head .lead {
  font-size: var(--fs-lead);
  color: var(--gray-700);
  line-height: 1.7;
  max-width: none;
  margin-inline: auto;
}
.section.dark .section-head .lead,
.section.dark-feature .section-head .lead { color: rgba(255,255,255,0.78); }

/* === Dramatic dark-feature section (homepage Support featured card style) === */
.section.dark-feature {
  background:
    radial-gradient(circle at 92% 8%, rgba(232, 93, 31, 0.32) 0%, transparent 50%),
    radial-gradient(circle at 8% 95%, rgba(251, 169, 130, 0.16) 0%, transparent 55%),
    linear-gradient(135deg, var(--ink-900) 0%, var(--ink-800) 60%, var(--ink-700) 100%);
  color: var(--white);
  border-radius: 32px;
  margin-inline: var(--gutter);
  position: relative;
  overflow: hidden;
}
.section.dark-feature::before {
  content: "";
  position: absolute;
  width: 340px; height: 340px;
  border-radius: 50%;
  background: var(--orange-500);
  opacity: 0.18;
  top: -120px; right: -100px;
  pointer-events: none;
  z-index: 0;
}
.section.dark-feature::after {
  content: "";
  position: absolute;
  width: 240px; height: 240px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.10;
  bottom: -100px; left: -60px;
  pointer-events: none;
  z-index: 0;
}
.section.dark-feature > .wrap { position: relative; z-index: 1; }
.section.dark-feature h2,
.section.dark-feature h3 { color: var(--white); }
.section.dark-feature p { color: rgba(255,255,255,0.78); }
.section.dark-feature .eyebrow { color: var(--orange-300); }
.section.dark-feature .eyebrow::before { background: var(--orange-400); }
.section.dark-feature .feature-card {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.section.dark-feature .feature-card:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--orange-400);
  transform: translateY(-4px);
  box-shadow: 0 18px 36px -16px rgba(0, 0, 0, 0.5);
}
.section.dark-feature .feature-card h3 { color: var(--white); }
.section.dark-feature .feature-card p { color: rgba(255,255,255,0.7); }
.section.dark-feature .feature-card .num { color: var(--orange-300); }

/* 5-phase grid + 6th outcome card */
.section.dark-feature .feature-grid.five-up {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.25rem;
}
@media (max-width: 900px) {
  .section.dark-feature .feature-grid.five-up { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 560px) {
  .section.dark-feature .feature-grid.five-up { grid-template-columns: 1fr; }
}

/* Phase outcome — live status mockup card */
.section.dark-feature .phase-outcome {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: var(--r-card);
  padding: 1.5rem;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  display: flex;
  flex-direction: column;
  gap: 1rem;
  position: relative;
  overflow: hidden;
  transition: transform 350ms cubic-bezier(0.4, 0, 0.2, 1),
              border-color 200ms ease,
              box-shadow 350ms ease;
}
.section.dark-feature .phase-outcome::before {
  content: "";
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 100% 0%, rgba(232, 93, 31, 0.22) 0%, transparent 65%);
  pointer-events: none;
}
.section.dark-feature .phase-outcome:hover {
  transform: translateY(-4px);
  border-color: var(--orange-400);
  box-shadow: 0 18px 36px -16px rgba(0, 0, 0, 0.5);
}
.section.dark-feature .phase-outcome > * { position: relative; z-index: 1; }
.section.dark-feature .phase-outcome .po-head {
  display: flex; align-items: center; justify-content: space-between; gap: 0.5rem;
}
.section.dark-feature .phase-outcome .po-live {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-body);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--orange-300);
}
.section.dark-feature .phase-outcome .po-live .pulse {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--orange-400);
  animation: pulse 2s ease-in-out infinite;
  box-shadow: 0 0 0 4px rgba(232, 93, 31, 0.16);
}
.section.dark-feature .phase-outcome .po-dots { display: flex; gap: 4px; }
.section.dark-feature .phase-outcome .po-dots span {
  width: 6px; height: 6px; border-radius: 50%; background: rgba(255, 255, 255, 0.2);
}
.section.dark-feature .phase-outcome .po-title {
  font-size: 0.78rem; color: rgba(255, 255, 255, 0.65); letter-spacing: 0.02em;
}
.section.dark-feature .phase-outcome .po-stat {
  display: flex; flex-direction: column; gap: 0.15rem;
}
.section.dark-feature .phase-outcome .po-num {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(2.5rem, 4vw, 3.25rem);
  line-height: 1;
  letter-spacing: -0.03em;
  color: var(--white);
}
.section.dark-feature .phase-outcome .po-num .po-unit {
  font-size: 0.42em; color: rgba(255, 255, 255, 0.55);
  margin-left: 0.25em; font-weight: 500; letter-spacing: 0;
}
.section.dark-feature .phase-outcome .po-sublabel {
  font-size: 0.78rem; color: rgba(255, 255, 255, 0.6);
}
.section.dark-feature .phase-outcome .po-spark {
  width: 100%; height: 50px; color: var(--orange-400); margin-top: auto;
}
.section.dark-feature .phase-outcome .po-checks {
  display: flex; flex-direction: column; gap: 0.45rem;
  padding-top: 0.85rem; border-top: 1px solid rgba(255, 255, 255, 0.10);
}
.section.dark-feature .phase-outcome .po-checks span {
  display: flex; align-items: center; gap: 0.55rem;
  font-size: 0.78rem; color: rgba(255, 255, 255, 0.78);
}
.section.dark-feature .phase-outcome .po-checks span::before {
  content: ""; display: inline-block;
  width: 14px; height: 14px; border-radius: 50%;
  background: rgba(232, 93, 31, 0.25);
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FBA982' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'><polyline points='20 6 9 17 4 12'/></svg>");
  background-repeat: no-repeat; background-position: center; background-size: 9px;
  flex-shrink: 0;
}

/* === Spacing rule between back-to-back dark sections === */
.section.dark-feature + .section.dark,
.section.dark + .section.dark-feature {
  margin-top: clamp(2rem, 4vw, 3.5rem);
}

/* === Warm-bg-rich (used on How we engage) — full-width gradient + blobs === */
.section.warm-bg-rich {
  background: linear-gradient(180deg, var(--orange-50) 0%, var(--cream) 100%);
  margin-inline: 0;
  border-radius: 0;
  position: relative;
  overflow: hidden;
}
.section.warm-bg-rich::before {
  content: "";
  position: absolute;
  width: 420px; height: 420px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.18;
  top: 25%; right: -200px;
  pointer-events: none;
  z-index: 0;
}
.section.warm-bg-rich::after {
  content: "";
  position: absolute;
  width: 280px; height: 280px;
  border-radius: 50%;
  background: var(--orange-500);
  opacity: 0.06;
  bottom: -100px; left: -100px;
  pointer-events: none;
  z-index: 0;
}
.section.warm-bg-rich > .wrap { position: relative; z-index: 1; }

/* === Process timeline compact 2x2 variant === */
.process-timeline.compact {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.25rem;
}
@media (max-width: 900px) {
  .process-timeline.compact { grid-template-columns: 1fr; }
}

/* Override .phase background + icon for warm-bg-rich context */
.process-timeline .phase {
  background: var(--white);
  border: 1px solid var(--orange-100);
  display: grid;
  grid-template-columns: 64px 1fr;
  gap: 1.5rem;
  transition: border-color 200ms, transform 250ms, box-shadow 250ms;
}
.process-timeline .phase:hover {
  border-color: var(--orange-300);
  transform: translateX(4px);
  box-shadow: 0 16px 32px -16px rgba(14, 23, 41, 0.12);
}
.process-timeline .phase .phase-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  background: var(--orange-100);
  color: var(--orange-700);
  display: grid;
  place-items: center;
  align-self: start;
  transition: background 250ms ease, color 250ms ease,
              transform 350ms cubic-bezier(0.34, 1.56, 0.64, 1);
}
.process-timeline .phase:hover .phase-icon {
  background: var(--orange-500);
  color: var(--white);
  transform: scale(1.08) rotate(-6deg);
}

/* === Deliverables strip — horizontal card grid (replaces vertical list) === */
.deliverables-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  list-style: none;
  margin: 0;
  padding: 0;
}
.deliverables-strip li {
  background: var(--white);
  border: 1px solid var(--gray-100);
  border-radius: var(--r-card);
  padding: 1.25rem;
  position: relative;
  font-size: 0.92rem;
  color: var(--gray-700);
  line-height: 1.5;
  transition: border-color 200ms, transform 200ms, box-shadow 200ms;
}
.deliverables-strip li:hover {
  border-color: var(--orange-300);
  transform: translateY(-3px);
  box-shadow: 0 12px 24px -10px rgba(14, 23, 41, 0.10);
}
.deliverables-strip li::before {
  content: "";
  display: block;
  width: 26px; height: 26px;
  border-radius: 50%;
  background: var(--orange-100);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23E85D1F' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='20 6 9 17 4 12'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 14px;
  margin-bottom: 0.85rem;
}
.deliverables-strip li strong {
  display: block;
  font-weight: 700;
  color: var(--ink);
  margin-bottom: 0.35rem;
  font-size: 0.98rem;
}

/* === Outcomes (By the numbers) — bigger numbers + white cards === */
.outcomes .o {
  padding: 1.75rem 1.5rem 1.75rem 1.75rem;
  background: var(--white);
  border-radius: var(--r-card);
  border-left: 4px solid var(--orange-500);
  box-shadow: 0 6px 18px -10px rgba(14, 23, 41, 0.16);
  transition: transform 250ms ease, box-shadow 250ms ease;
}
.outcomes .o:hover {
  transform: translateY(-4px);
  box-shadow: 0 18px 32px -16px rgba(14, 23, 41, 0.18);
}
.outcomes .o .num {
  font-size: clamp(2.25rem, 3.6vw, 3.25rem) !important;
  font-weight: 800 !important;
  letter-spacing: -0.035em;
  line-height: 1;
  display: block;
  margin-bottom: 0.5rem !important;
}
.outcomes .o .lbl {
  font-size: 0.92rem;
  color: var(--gray-700);
  line-height: 1.5;
}

/* === FAQ centered under section-head === */
.section .faq {
  margin-inline: auto;
  max-width: 760px;
}

/* === Orange testimonial section === */
.section.testimonial-orange,
.section.bfm-callout {
  background:
    radial-gradient(circle at 92% 12%, rgba(255, 255, 255, 0.18) 0%, transparent 55%),
    radial-gradient(circle at 6% 92%, rgba(14, 23, 41, 0.10) 0%, transparent 55%),
    linear-gradient(135deg, var(--orange-400) 0%, var(--orange-500) 60%, var(--orange-600) 100%);
  color: var(--white);
  border-radius: 32px;
  margin-inline: var(--gutter);
  margin-block: clamp(1.5rem, 3vw, 2.5rem);
  padding-block: clamp(1.5rem, 3vw, 2.5rem) !important;
  position: relative;
  overflow: hidden;
  isolation: isolate;
}
.section.bfm-callout h2,
.section.bfm-callout h3 { color: var(--white); }
.section.bfm-callout .eyebrow { color: var(--white); }
.section.bfm-callout .eyebrow::before { background: var(--ink-900); }
.section.bfm-callout h2 em {
  color: var(--ink-900);
  font-weight: 700;
  font-style: italic;
}
.bfm-tags {
  list-style: none;
  padding: 0;
  margin: clamp(1.25rem, 2vw, 1.75rem) auto 0;
  max-width: 920px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 0.6rem 0.7rem;
}
.bfm-tags li {
  background: rgba(255, 255, 255, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.28);
  backdrop-filter: blur(6px);
  -webkit-backdrop-filter: blur(6px);
  color: var(--white);
  padding: 0.55rem 1.05rem;
  border-radius: var(--r-pill);
  font-family: var(--font-display);
  font-weight: 500;
  font-size: 0.95rem;
  letter-spacing: -0.005em;
  transition: background 200ms, border-color 200ms, transform 200ms;
}
.bfm-tags li:hover {
  background: var(--ink-900);
  border-color: var(--ink-900);
  transform: translateY(-2px);
}

.section.testimonial-orange::before {
  content: "";
  position: absolute;
  width: 380px; height: 380px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.35;
  top: -160px; right: -120px;
  pointer-events: none;
  z-index: 0;
}
.section.testimonial-orange::after {
  content: "";
  position: absolute;
  width: 260px; height: 260px;
  border-radius: 50%;
  background: var(--ink-900);
  opacity: 0.10;
  bottom: -120px; left: -80px;
  pointer-events: none;
  z-index: 0;
}
.section.testimonial-orange > .wrap { position: relative; z-index: 1; }

.testimonial-layout {
  display: grid;
  grid-template-columns: minmax(220px, 300px) 1fr;
  gap: clamp(1.75rem, 4vw, 4rem);
  align-items: center;
}
.testimonial-layout .testimonial-photo {
  aspect-ratio: 4 / 5;
  position: relative;
  z-index: 1;
}
.testimonial-layout .testimonial-photo img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-radius: 60% 40% 50% 60% / 55% 50% 50% 60%;
  box-shadow: 0 22px 44px -18px rgba(14, 23, 41, 0.45);
  position: relative;
  z-index: 2;
}
.testimonial-layout .testimonial-photo .testimonial-blob {
  position: absolute;
  width: 80%;
  height: 80%;
  bottom: -6%;
  right: -8%;
  background: var(--ink-900);
  opacity: 0.18;
  border-radius: 40% 60% 60% 40% / 50% 60% 40% 50%;
  z-index: 1;
}
.testimonial-layout .testimonial-quote .quote-text {
  font-family: var(--font-display);
  font-weight: 500;
  font-size: clamp(1.15rem, 1.9vw, 1.55rem);
  line-height: 1.35;
  letter-spacing: -0.012em;
  color: var(--white);
  margin-bottom: 1.25rem;
  position: relative;
}
.testimonial-layout .testimonial-quote .quote-text::before {
  content: "\\201C";
  font-family: var(--font-display);
  font-weight: 800;
  font-size: 3rem;
  color: rgba(255, 255, 255, 0.35);
  position: absolute;
  top: -1.6rem;
  left: -0.6rem;
  line-height: 1;
  pointer-events: none;
}
.testimonial-layout .testimonial-quote .quote-text em {
  font-style: italic;
  font-weight: 700;
  color: var(--ink-900);
}
.testimonial-layout .testimonial-quote .quote-attr {
  display: inline-flex;
  align-items: center;
  gap: 0.85rem;
  background: rgba(255, 255, 255, 0.16);
  border: 1px solid rgba(255, 255, 255, 0.28);
  padding: 0.55rem 1.1rem 0.55rem 0.55rem;
  border-radius: var(--r-pill);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}
.testimonial-layout .testimonial-quote .quote-attr .avatar {
  width: 36px; height: 36px;
  border-radius: 50%;
  background: var(--ink-900);
  color: var(--white);
  display: grid; place-items: center;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 0.04em;
}
.testimonial-layout .testimonial-quote .quote-attr .who {
  display: flex; flex-direction: column;
  line-height: 1.25;
  text-align: left;
}
.testimonial-layout .testimonial-quote .quote-attr .who strong {
  font-weight: 700;
  font-size: 0.92rem;
  color: var(--white);
}
.testimonial-layout .testimonial-quote .quote-attr .who span {
  font-size: 0.78rem;
  color: rgba(255, 255, 255, 0.78);
}
@media (max-width: 800px) {
  .testimonial-layout { grid-template-columns: 1fr; }
  .testimonial-layout .testimonial-photo { max-width: 360px; }
}

/* === Big page-closing CTA === */
.cta-big {
  position: relative;
  background:
    radial-gradient(circle at 92% 12%, rgba(232, 93, 31, 0.42) 0%, transparent 50%),
    radial-gradient(circle at 8% 92%, rgba(251, 169, 130, 0.22) 0%, transparent 55%),
    linear-gradient(135deg, var(--ink-900) 0%, var(--ink-800) 60%, var(--ink-700) 100%);
  color: var(--white);
  border-radius: 36px;
  padding: clamp(2.75rem, 5vw, 4.5rem) clamp(2rem, 4.5vw, 4rem);
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: clamp(2rem, 4vw, 4rem);
  align-items: center;
  overflow: hidden;
  isolation: isolate;
}
.cta-big::before {
  content: "";
  position: absolute;
  width: 460px; height: 460px;
  border-radius: 50%;
  background: var(--orange-500);
  opacity: 0.16;
  top: -180px; right: -120px;
  pointer-events: none;
  z-index: 0;
}
.cta-big::after {
  content: "";
  position: absolute;
  width: 320px; height: 320px;
  border-radius: 50%;
  background: var(--orange-300);
  opacity: 0.10;
  bottom: -160px; left: -80px;
  pointer-events: none;
  z-index: 0;
}
.cta-big > * { position: relative; z-index: 1; }
.cta-big-copy { display: flex; flex-direction: column; align-items: flex-start; }
.cta-big-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  font-family: var(--font-body);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--orange-300);
  margin-bottom: 1.25rem;
}
.cta-big-eyebrow::before {
  content: "";
  width: 1.5rem;
  height: 1px;
  background: var(--orange-500);
  display: inline-block;
}
.cta-big h2 {
  color: var(--white);
  font-size: clamp(2rem, 3.6vw, 3.25rem);
  line-height: 1.05;
  letter-spacing: -0.025em;
  margin-bottom: 1.1rem;
  max-width: 18ch;
}
.cta-big h2 em {
  color: var(--orange-300);
  font-style: italic;
  font-weight: 500;
}
.cta-big p {
  color: rgba(255, 255, 255, 0.78);
  font-size: clamp(1rem, 1.2vw, 1.15rem);
  line-height: 1.65;
  max-width: 52ch;
  margin-bottom: 1.5rem;
}
.cta-big-features {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.7rem;
}
.cta-big-features li {
  position: relative;
  padding-left: 1.85rem;
  color: rgba(255, 255, 255, 0.82);
  font-size: 0.95rem;
  line-height: 1.5;
}
.cta-big-features li::before {
  content: "";
  position: absolute;
  left: 0; top: 4px;
  width: 18px; height: 18px;
  border-radius: 50%;
  background: rgba(232, 93, 31, 0.22);
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23FBA982' stroke-width='3.5' stroke-linecap='round' stroke-linejoin='round'><polyline points='20 6 9 17 4 12'/></svg>");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 11px;
}
.btn-big {
  background: var(--orange-500);
  color: var(--white);
  padding: 1.15rem 2rem;
  font-size: 1rem;
  font-weight: 700;
  letter-spacing: 0.01em;
  box-shadow: 0 14px 28px -10px rgba(232, 93, 31, 0.45);
}
.btn-big:hover {
  background: var(--orange-700);
  transform: translateY(-2px);
  box-shadow: 0 18px 32px -10px rgba(232, 93, 31, 0.55);
}
.cta-big-aside {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  align-items: flex-start;
}
.cta-big-stat {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.10);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  padding: 1.85rem 2rem;
  border-radius: 24px;
  width: 100%;
}
.cta-big-stat-num {
  font-family: var(--font-display);
  font-weight: 800;
  font-size: clamp(4.5rem, 8vw, 6.5rem);
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--orange-300);
  display: block;
  margin-bottom: 0.6rem;
}
.cta-big-stat-num .cta-big-stat-unit {
  font-size: 0.4em;
  color: rgba(255, 255, 255, 0.6);
  margin-left: 0.3em;
  font-weight: 500;
  letter-spacing: 0;
}
.cta-big-stat-lbl {
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.65);
  letter-spacing: 0.02em;
  line-height: 1.5;
}
.cta-big-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.65rem;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.14);
  padding: 0.55rem 1rem;
  border-radius: var(--r-pill);
  font-size: 0.78rem;
  font-weight: 500;
  letter-spacing: 0.02em;
  color: rgba(255, 255, 255, 0.85);
}
.cta-big-badge .pulse {
  display: inline-block;
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--orange-500);
  animation: pulse 2s ease-in-out infinite;
}
@media (max-width: 900px) {
  .cta-big { grid-template-columns: 1fr; padding: 2.5rem; }
  .cta-big-aside { align-items: stretch; }
}
"""


# ============================================================
# Header / Footer / Layout
# ============================================================
def header(active: str = ""):
    """active is the page key used to mark active nav state."""
    def cls(key):
        return ' class="active"' if active == key else ''
    def li_cls(key):
        return ' active' if active == key else ''
    return f"""  <header class="site-header">
    <div class="wrap nav">
      <a href="index.html" class="brand" aria-label="Buoy Consulting home">
        <span class="brand-logo" role="img" aria-label="Buoy Consulting logo"></span>
        <span class="brand-text">
          <span class="brand-name">Buoy</span>
          <span class="brand-tag">Consulting</span>
        </span>
      </a>

      <nav aria-label="Primary">
        <ul class="nav-links">
          <li><a href="index.html"{cls('home')}>Home</a></li>
          <li><a href="about.html"{cls('about')}>About</a></li>
          <li class="has-dropdown{li_cls('services')}">
            <a href="services.html"{cls('services')}>Services</a>
            <div class="dropdown" role="menu">
              <div class="dropdown-card">
                <div class="dropdown-grid">
                  <div class="dropdown-col">
                    <h6>Core Services</h6>
                    <ul>
                      <li><a href="implementation.html">
                        <span>
                          Implementation
                          <span class="item-desc">Rollouts &amp; migrations</span>
                        </span>
                        <span class="item-arr">→</span>
                      </a></li>
                      <li><a href="process-improvement.html">
                        <span>
                          Process Improvement
                          <span class="item-desc">Audit, refine, rebuild</span>
                        </span>
                        <span class="item-arr">→</span>
                      </a></li>
                      <li><a href="training.html">
                        <span>
                          Training
                          <span class="item-desc">Hands-on Jobpac sessions</span>
                        </span>
                        <span class="item-arr">→</span>
                      </a></li>
                      <li><a href="civil-construction.html">
                        <span>
                          Civil &amp; Construction
                          <span class="item-desc">Industry specialisation</span>
                        </span>
                        <span class="item-arr">→</span>
                      </a></li>
                    </ul>
                  </div>
                  <div class="dropdown-col">
                    <h6>Support Services</h6>
                    <ul>
                      <li><a href="support-bookkeeping.html"><span>Bookkeeping</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-accounts-payable.html"><span>Accounts Payable</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-accounts-receivable.html"><span>Accounts Receivable</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-payroll.html"><span>Payroll</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-profit-loss.html"><span>Profit &amp; Loss</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-temp-relief.html"><span>Temp Relief</span><span class="item-arr">→</span></a></li>
                      <li><a href="support-business-forecasting.html"><span>Business Forecasting</span><span class="item-arr">→</span></a></li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
          </li>
          <li><a href="contact.html"{cls('contact')}>Contact</a></li>
        </ul>
      </nav>

      <div class="nav-actions">
        <a href="contact.html" class="btn btn-primary nav-cta">Book a consultation</a>
      </div>
    </div>
  </header>"""

FOOTER = """  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand" aria-label="Buoy Consulting home">
            <span class="brand-logo" role="img" aria-label="Buoy Consulting logo"></span>
            <span class="brand-text">
              <span class="brand-name">Buoy</span>
              <span class="brand-tag">Consulting</span>
            </span>
          </a>
          <p>Specialist Jobpac consulting for construction and civil businesses across Australia and New Zealand.</p>
          <div class="contact">
            <a href="mailto:info@buoyconsultancy.com.au">info@buoyconsultancy.com.au</a>
            <a href="tel:+61292345678">+61 2 9234 5678</a>
          </div>
        </div>

        <div class="footer-col">
          <h5>Services</h5>
          <ul>
            <li><a href="implementation.html">Implementation</a></li>
            <li><a href="process-improvement.html">Process Improvement</a></li>
            <li><a href="training.html">Training</a></li>
            <li><a href="civil-construction.html">Civil &amp; Construction</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Support</h5>
          <ul>
            <li><a href="support-bookkeeping.html">Bookkeeping</a></li>
            <li><a href="support-accounts-payable.html">Accounts Payable</a></li>
            <li><a href="support-accounts-receivable.html">Accounts Receivable</a></li>
            <li><a href="support-payroll.html">Payroll</a></li>
            <li><a href="support-profit-loss.html">Profit &amp; Loss</a></li>
            <li><a href="support-temp-relief.html">Temp Relief</a></li>
            <li><a href="support-business-forecasting.html">Business Forecasting</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h5>Company</h5>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="about.html#team">Team</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>© 2026 Buoy Consulting Pty Ltd. All rights reserved.</div>
        <div class="legal">
          <a href="#">Privacy</a>
          <a href="#">Terms</a>
        </div>
      </div>
    </div>
  </footer>"""

REVEAL_SCRIPT = """  <script>
    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      document.querySelectorAll('.reveal').forEach((el, i) => {
        el.style.transitionDelay = `${Math.min(i * 60, 300)}ms`;
        io.observe(el);
      });
    } else {
      document.querySelectorAll('.reveal').forEach(el => el.classList.add('in'));
    }

    // Accordion: opening one FAQ closes any others in the same group
    document.querySelectorAll('.faq').forEach(group => {
      group.querySelectorAll(':scope > details').forEach(d => {
        d.addEventListener('toggle', () => {
          if (!d.open) return;
          group.querySelectorAll(':scope > details[open]').forEach(other => {
            if (other !== d) other.open = false;
          });
        });
      });
    });
  </script>"""


def cta_big(eyebrow: str, headline_html: str, lead: str, features: list,
            stat_num_html: str, stat_label: str, badge_text: str = "Senior consultant on the call"):
    """Big page-closing CTA — two-column dark gradient box with feature list
    on the left and a glassy stat aside on the right."""
    features_html = "".join(f"            <li>{f}</li>\n" for f in features)
    return f"""    <section class="section">
      <div class="wrap">
        <div class="cta-big reveal">
          <div class="cta-big-copy">
            <span class="cta-big-eyebrow">{eyebrow}</span>
            <h2>{headline_html}</h2>
            <p>{lead}</p>
            <ul class="cta-big-features">
{features_html}            </ul>
            <a href="contact.html" class="btn btn-primary btn-big">Book a consultation <span class="arr">→</span></a>
          </div>
          <div class="cta-big-aside" aria-hidden="true">
            <div class="cta-big-stat">
              <span class="cta-big-stat-num">{stat_num_html}</span>
              <span class="cta-big-stat-lbl">{stat_label}</span>
            </div>
            <div class="cta-big-badge"><span class="pulse"></span>{badge_text}</div>
          </div>
        </div>
      </div>
    </section>"""


def cta_block(headline: str, sub: str = "Tell us where you're stuck. The first call is free, no slide deck."):
    """Legacy small inline-cta. Kept for any page that still uses it; new pages
    should use cta_big() instead."""
    return f"""        <div class="inline-cta reveal">
          <div class="cta-text">
            <h2>{headline}</h2>
            <p>{sub}</p>
          </div>
          <div class="cta-actions">
            <a href="contact.html" class="btn btn-primary">Book a consultation <span class="arr">→</span></a>
            <a href="services.html" class="btn btn-ghost">All services</a>
          </div>
        </div>"""


def page_hero(eyebrow: str, h1: str, lead: str, banner: str = "", center: bool = False):
    cls = "page-hero center" if center else "page-hero"
    banner_html = f'<div class="same-day-banner reveal"><span class="pulse"></span>{banner}</div>' if banner else ''
    return f"""    <section class="{cls}">
      <div class="wrap">
        <div class="reveal">
          {banner_html}
          <span class="eyebrow">{eyebrow}</span>
          <h1>{h1}</h1>
          <p class="lead">{lead}</p>
        </div>
      </div>
    </section>"""


def hero_with_visual(eyebrow: str, h1: str, lead: str, image_src: str, image_alt: str,
                     badge: str = "", banner: str = "", float_stat=None):
    """h1 can include <em>…</em> for italic emphasis on a key word.
    float_stat is an optional dict like {'num': '11 wks', 'lbl': 'avg go-live', 'icon': 'arrow'}.
    """
    banner_html = f'<div class="same-day-banner reveal"><span class="pulse"></span>{banner}</div>' if banner else ''
    badge_html = f'<span class="badge"><span class="pulse"></span>{badge}</span>' if badge else ''
    float_html = ""
    if float_stat:
        icon_svg = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="7 17 17 7"/><polyline points="7 7 17 7 17 17"/></svg>'
        float_html = f"""            <div class="hero-float-card reveal">
              <div class="hf-icon" aria-hidden="true">{icon_svg}</div>
              <div class="hf-meta"><b>{float_stat['num']}</b><span>{float_stat['lbl']}</span></div>
            </div>"""
    return f"""    <section class="page-hero with-visual">
      <div class="wrap">
        <div class="hero-grid">
          <div class="hero-text reveal">
            {banner_html}
            <span class="eyebrow">{eyebrow}</span>
            <h1>{h1}</h1>
            <p class="lead">{lead}</p>
          </div>
          <div class="hero-visual-card-wrap">
            <div class="hero-visual-card reveal" aria-hidden="true">
              <div class="blob-accent"></div>
              <img src="{image_src}" alt="{image_alt}" loading="lazy" />
              {badge_html}
            </div>
{float_html}
          </div>
        </div>
      </div>
    </section>"""


def process_section():
    """Buoy engagement process — identical content across all service pages.
    Uses the full-width warm-bg-rich treatment with a compact 2x2 grid of
    icon-led phase cards (mirrors the homepage 'How we engage' section)."""
    DISCOVERY_ICON = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>'
    SCOPE_ICON = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>'
    EXECUTE_ICON = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>'
    EMBED_ICON = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
    return f"""    <section class="section warm-bg-rich">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">How we engage</span>
          <h2>Four steps. No surprises. No bait&#8209;and&#8209;switch.</h2>
          <p class="lead">Every Buoy engagement runs the same way &mdash; fixed scope, senior consultant, full transparency end&#8209;to&#8209;end.</p>
        </div>
        <div class="process-timeline compact">
          <div class="phase reveal">
            <div class="phase-icon" aria-hidden="true">{DISCOVERY_ICON}</div>
            <div>
              <div class="duration">Discovery &middot; 30&ndash;60 minutes &middot; no cost</div>
              <h3>We listen first.</h3>
              <p>A no-cost call. We learn your current Jobpac setup, what's hurting most, and what's already worked. You're talking to the senior consultant who'd actually do the work &mdash; not a sales person reading off a script.</p>
            </div>
          </div>
          <div class="phase reveal">
            <div class="phase-icon" aria-hidden="true">{SCOPE_ICON}</div>
            <div>
              <div class="duration">Scope &middot; 3&ndash;7 business days</div>
              <h3>You get a fixed-scope proposal.</h3>
              <p>Deliverables, timeline, price, and the named senior consultant who'll lead the engagement &mdash; in writing, within a week. No &ldquo;T&amp;E to be confirmed.&rdquo; The price is the price.</p>
            </div>
          </div>
          <div class="phase reveal">
            <div class="phase-icon" aria-hidden="true">{EXECUTE_ICON}</div>
            <div>
              <div class="duration">Execute &middot; duration varies by scope</div>
              <h3>Senior consultant on the keys.</h3>
              <p>The person on the proposal does the work. Not a junior. Not a partner who hands it down. Weekly written status, risks called out the week they emerge &mdash; not the week before go-live.</p>
            </div>
          </div>
          <div class="phase reveal">
            <div class="phase-icon" aria-hidden="true">{EMBED_ICON}</div>
            <div>
              <div class="duration">Embed &middot; final 1&ndash;2 weeks of every engagement</div>
              <h3>Your team owns it when we leave.</h3>
              <p>Documentation, hands-on training, and a structured handover &mdash; written so your team can run it long after we're gone. Optional ongoing same-day support after handover, but you're never locked in.</p>
            </div>
          </div>
        </div>
      </div>
    </section>"""


def faq_section(questions: list, eyebrow: str = "Common questions", heading: str = "What people usually ask."):
    """questions is a list of (question, answer) tuples."""
    items = "\n          ".join(
        f"""<details>
            <summary>{q}</summary>
            <p>{a}</p>
          </details>"""
        for q, a in questions
    )
    return f"""    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">{eyebrow}</span>
          <h2>{heading}</h2>
        </div>
        <div class="faq reveal">
          {items}
        </div>
      </div>
    </section>"""


def testimonial_section(quote_html: str, attr_initials: str, attr_role: str, attr_meta: str,
                        portrait_src: str = "client-portrait.jpg", portrait_alt: str = "Client portrait"):
    """Orange-saturated testimonial with a blob-shaped portrait on the left
    and the quote + attribution chip on the right."""
    return f"""    <section class="section testimonial-orange reveal">
      <div class="wrap">
        <div class="testimonial-layout">
          <div class="testimonial-photo">
            <div class="testimonial-blob"></div>
            <img src="{portrait_src}" alt="{portrait_alt}" loading="lazy" />
          </div>
          <div class="testimonial-quote">
            <p class="quote-text">{quote_html}</p>
            <div class="quote-attr">
              <div class="avatar">{attr_initials}</div>
              <div class="who">
                <strong>{attr_role}</strong>
                <span>{attr_meta}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>"""


def stat_ticker_section(items: list):
    """Edge-to-edge animated stat strip on dark background.
    items: list of (num, lbl) tuples — duplicated to make the loop seamless."""
    pairs = items + items  # duplicate for seamless loop
    spans = "\n          ".join(
        f'<div class="item"><span class="num">{n}</span><span class="lbl">{l}</span></div>'
        for n, l in pairs
    )
    return f"""    <section class="stat-ticker reveal" aria-hidden="true">
      <div class="stat-ticker-track">
          {spans}
      </div>
    </section>"""


def stats_section(eyebrow: str, heading: str, items: list):
    """items is a list of (num, lbl) tuples for the outcomes block.
    Sits on plain cream so the white shadowed cards (from .outcomes .o) pop."""
    outcomes = "\n          ".join(
        f'<div class="o"><span class="num">{n}</span><span class="lbl">{l}</span></div>'
        for n, l in items
    )
    return f"""    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">{eyebrow}</span>
          <h2>{heading}</h2>
        </div>
        <div class="outcomes reveal" style="margin-top: 2rem;">
          {outcomes}
        </div>
      </div>
    </section>"""


def make_layout(title: str, description: str, active: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — Buoy Consulting</title>
  <meta name="description" content="{description}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet" />
  <link href="https://api.fontshare.com/v2/css?f[]=cabinet-grotesk@800,700,500,400&display=swap" rel="stylesheet" />

  <link rel="stylesheet" href="styles.css?v={CSS_VERSION}" />
</head>
<body>

{header(active)}

  <main>
{body}
  </main>

{FOOTER}

{REVEAL_SCRIPT}
</body>
</html>
"""


# ============================================================
# Page bodies
# ============================================================
PAGES = {}

# -------- About (merged with team) --------
PAGES["about.html"] = dict(
    title="About",
    description="Buoy Consulting — Australia and New Zealand's specialist Jobpac consultancy for construction and civil businesses. Founded 2010. Six senior consultants, 100+ years combined experience.",
    active="about",
    body=hero_with_visual(
        "About Buoy",
        "Specialist Jobpac consultants &mdash; people who've <em>actually</em> worked in construction businesses.",
        "Buoy Consulting was founded in 2010 by senior finance and construction operators who'd spent decades inside the industry. Sixteen years on, focused exclusively on Jobpac for construction and civil businesses throughout Australia and New Zealand.",
        image_src="office-team.jpg",
        image_alt="Buoy consultants at work in a construction finance office",
        badge="Independent &middot; Senior-led",
        float_stat={"num": "16 yrs", "lbl": "specialising in Jobpac"},
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="two-col aside reveal">
          <div>
            <h2>Why we exist.</h2>
            <p>We are unique. Every consultant on our team has spent at least fifteen years inside a construction or civil business doing the work &mdash; running projects, variations, subcontracting, retentions, claims to the client, month-end, financials, every task that needs to be performed. We know what it feels like to have the CM wanting your cost reports in the morning and dealing with a CFO who needs the cash forecast in the morning.</p>
            <p>That's not a bio line. It's the reason our advice lands instead of bouncing off. When you tell us your retentions are out by $80k, we know exactly where to look first.</p>
            <p>Sixteen years in, we've watched the industry move through three software cycles, two recessions, a once-in-a-century supply chain shock, and the slow shift from spreadsheet-driven cost control to integrated project ERPs. Every one of those shifts has played out in our clients' businesses. That's the perspective you're hiring.</p>
          </div>
          <div>
            <div class="outcomes">
              <div class="o"><span class="num">2010</span><span class="lbl">Founded by senior construction-finance operators</span></div>
              <div class="o"><span class="num">16</span><span class="lbl">years specialising in Jobpac</span></div>
              <div class="o"><span class="num">6</span><span class="lbl">senior consultants on the bench</span></div>
              <div class="o"><span class="num">100+</span><span class="lbl">years combined construction experience</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">How we're different</span>
          <h2>What you actually get when you hire Buoy.</h2>
          <p class="lead">A small consultancy is only worth hiring if &ldquo;small&rdquo; means something. Here's what it means in practice for our clients.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal">
            <div class="num">01 / Same-day support</div>
            <h3>Answered the same day, every day.</h3>
            <p>Not a 48-hour SLA. Not "next business day." Most tickets are answered within hours by a senior who can actually solve them. When month-end is tomorrow, that's the difference that matters.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">02 / No juniors</div>
            <h3>The senior who pitched does the work.</h3>
            <p>Most consultancies sell you the partner and deliver you a graduate. We don't have graduates. The person who scoped your engagement is the person sitting at the keyboard.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">03 / Vendor-independent</div>
            <h3>We don't sell licences.</h3>
            <p>We don't earn commission from your Jobpac subscription. We earn fees from making your existing investment deliver. That changes whose side we're on.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">04 / Construction-native</div>
            <h3>Civil, commercial, and building.</h3>
            <p>We've worked across Tier-2 builders, civil contractors, fit-out specialists, and family-owned regional businesses. We know what stage claims, retentions, and plant cost recovery look like in Jobpac because we've configured them ourselves.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">05 / Fixed scope, no surprises</div>
            <h3>Priced before we start.</h3>
            <p>Every engagement starts with a fixed-scope proposal. You see the price, the timeline, and the deliverables before you sign anything. We don't run the meter, and we don't surface "phase 2" scope after you've signed.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">06 / Embedded knowledge</div>
            <h3>Your team owns it when we leave.</h3>
            <p>Documentation, training, and a real handover. We're consultants &mdash; not a permanent dependency. The goal is for your team to run Jobpac without us, with confidence, by the time we walk out the door.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="team">
      <div class="wrap">
        <div class="reveal" style="text-align: center; max-width: 720px; margin: 0 auto 1rem;">
          <span class="eyebrow">Our team</span>
          <h2>Senior consultants. Decades of Jobpac.</h2>
          <p class="lead" style="margin: 1rem auto 0;">Every engagement is led by someone with at least fifteen years of construction or civil finance experience &mdash; not someone reading the manual back to you. Meet the people you'll actually work with.</p>
        </div>
        <div class="team-detail">
          <div class="person reveal">
            <div class="photo"><img src="donna-duff.jpg" alt="Donna Duff" loading="lazy" /></div>
            <h3>Donna Duff</h3>
            <p class="role">Founding Director</p>
            <p class="bio">Founded Buoy in 2010 after fifteen years in construction finance leadership at Tier-2 builders across Sydney. Donna leads strategy and is the senior consultant on most flagship engagements. CPA, BCom (UNSW).</p>
          </div>
          <div class="person reveal">
            <div class="photo"><img src="kylie-jane.jpg" alt="Kylie Jane" loading="lazy" /></div>
            <h3>Kylie Jane</h3>
            <p class="role">Senior Consultant</p>
            <p class="bio">Bio coming soon.</p>
          </div>
          <div class="person reveal">
            <div class="photo"><img src="janitta-weis.jpg" alt="Janitta Weis" loading="lazy" /></div>
            <h3>Janitta Weis</h3>
            <p class="role">Senior Consultant</p>
            <p class="bio">Janitta Weis provides specialist construction finance, bookkeeping, systems, payroll, and project administration support to businesses operating in the construction and development sectors. With practical experience using Jobpac and a range of payroll systems, Janitta supports clients across the full finance administration cycle, including accounts payable, accounts receivable, progress claims, payroll support, month-end reconciliations, journals, BAS and GST reconciliation support, project financial setup, cost code structures, budget allocation, and reporting integrity.</p>
            <p class="bio">Her experience includes assisting businesses with Jobpac implementation and clean-up, project budget alignment, cost codes and GL setup support, BFM processes, project reporting, financial completion, and reconciliation of system-generated accounts. Janitta also provides end-to-end bookkeeping support and assists accountants with month-end processes and financial reporting requirements.</p>
            <p class="bio">As being a pass subcontractor, Janitta can provide hands-on operational support, system review, process improvement, training assistance, and practical guidance to help clients stabilise their finance, bookkeeping, payroll, and project reporting processes. Her approach is detail-focused, commercially aware, and grounded in ensuring that financial information is reliable, well-structured, and useful for decision-making.</p>
          </div>
          <div class="person reveal">
            <div class="photo photo-placeholder" aria-hidden="true"><span>MD</span></div>
            <h3>Matthew Duly</h3>
            <p class="role">Senior Trainer</p>
            <p class="bio">Matthew Duly has over 35 years&rsquo; experience as a Project Commercial Manager on large and small infrastructure and building projects including highway, tunnel, bridge, water, services, office and hotel projects. Matthew worked with Baulderstone for 25 years and was one of the first users trained in Jobpac when Baulderstone commenced using Jobpac in 1990. He has experienced vast development in Jobpac over that period and lead a number of client requests for Jobpac development. He is an expert in the site operation of Jobpac for Lump Sum and Schedule of Rates projects, as well as Earned Value. As senior trainer at Buoy he has worked with many clients implementing Jobpac on sites and training the site team to use Jobpac.</p>
            <a class="person-social" href="http://www.linkedin.com/in/matthew-duly" target="_blank" rel="noopener" aria-label="Matthew Duly on LinkedIn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.55V9h3.57v11.45z"/></svg>
              <span>LinkedIn</span>
            </a>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="two-col aside reveal">
          <div>
            <h2>Why we stay deliberately small.</h2>
            <p>Most consultancies grow by adding juniors and reselling them at senior rates. We grow by adding seniors and selling them at senior rates &mdash; or not adding anyone at all. Six is enough to cover any engagement we'd take on, and small enough that you'll always know exactly who's doing the work.</p>
            <p>Every consultant on the team has at least fifteen years of construction or civil finance experience. We don't hire generalists and put them through a four-week Jobpac course. The bar to join Buoy is the bar that makes you valuable to a client on day one.</p>
            <p>It also keeps us honest. With a six-person team there's no place to hide an underperformer behind a partner's name on a proposal. Every consultant has to be able to walk into any client engagement and add value &mdash; because eventually they will.</p>
          </div>
          <div>
            <div class="outcomes">
              <div class="o"><span class="num">15+</span><span class="lbl">years experience minimum on every engagement</span></div>
              <div class="o"><span class="num">0</span><span class="lbl">graduates or junior consultants</span></div>
              <div class="o"><span class="num">100%</span><span class="lbl">construction-industry background</span></div>
              <div class="o"><span class="num">AU &amp; NZ</span><span class="lbl">on-site coverage from Sydney, Melbourne, Brisbane &amp; Auckland</span></div>
            </div>
          </div>
        </div>
      </div>
    </section>

""" + cta_big(
        eyebrow="Ready when you are",
        headline_html="Want to know if we're the <em>right fit</em>?",
        lead="A 30-minute call, no slide deck, no pressure. We'll tell you whether we can help &mdash; and if we can't, who would.",
        features=[
            "Senior consultant on the call &mdash; not a salesperson",
            "Straight read on whether we're a fit for your situation",
            "If we're not, we'll point you at someone who is",
        ],
        stat_num_html="16",
        stat_label="years specialising in Jobpac for AU/NZ construction",
        badge_text="Senior consultant on the call",
    ),
)

# -------- Services (overview) --------
PAGES["services.html"] = dict(
    title="Services",
    description="Specialist Jobpac services for construction and civil businesses: implementation, process improvement, training, support, and industry specialisation across AU and NZ.",
    active="services",
    body=page_hero(
        "What we do",
        "Specialist Jobpac services, <em>end&#8209;to&#8209;end</em>.",
        "From greenfield rollouts to ongoing finance support &mdash; whether you need a one-off project or a long-term partner, Buoy covers the full Jobpac lifecycle for construction and civil businesses across Australia and New Zealand.",
        center=True,
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="sub-grid">
          <a href="implementation.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">IM</div>
            <h3>Implementation</h3>
            <p>Greenfield rollouts, ERP migrations, and module-by-module deployments. Configured the way construction actually runs.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="process-improvement.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">PI</div>
            <h3>Process Improvement</h3>
            <p>Already running Jobpac but not getting the value you paid for? We audit, find the gaps, and rebuild the workflows around how your team really works.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support.html" class="sub-card reveal" style="text-decoration:none;color:inherit;background:linear-gradient(135deg, var(--ink-900), var(--ink-800));color:var(--white);border-color:transparent;">
            <div class="icon" style="background:rgba(232,93,31,0.18);color:var(--orange-300);">SD</div>
            <h3 style="color:var(--white);">Support</h3>
            <p style="color:rgba(255,255,255,0.8);"><strong style="color:var(--orange-300);">Same-day support, every day.</strong> Bookkeeping, AP/AR, payroll, P&amp;L, temp relief, and forecasting &mdash; on call or fully embedded.</p>
            <span class="more" style="color:var(--orange-300);">Explore Support <span class="arr">→</span></span>
          </a>
          <a href="training.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">TR</div>
            <h3>Training</h3>
            <p>Hands-on Jobpac training tailored to your modules, your team's experience level, and your real project workflows.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="civil-construction.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">CC</div>
            <h3>Civil &amp; Construction</h3>
            <p>Specialist focus on the unique mechanics of civil and commercial construction &mdash; subbie claims, retentions, plant costing, and stage billing.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
        </div>
      </div>
    </section>

""" + cta_big(
        eyebrow="Ready when you are",
        headline_html="Not sure where to <em>start</em>?",
        lead="Send us your situation in two sentences. We'll point you at the right service &mdash; or tell you straight if it isn't us.",
        features=[
            "30-minute scoping call, no obligation",
            "Senior consultant on the call from day one",
            "Fixed-scope proposal within the week",
        ],
        stat_num_html="5",
        stat_label="specialist Jobpac services for construction &amp; civil",
        badge_text="Senior consultant on the call",
    ),
)

# -------- Implementation --------
PAGES["implementation.html"] = dict(
    title="Implementation",
    description="Jobpac implementation, migration, and module deployment for construction and civil businesses. Fixed-scope, senior-led, configured the way construction actually runs.",
    active="services",
    body=hero_with_visual(
        "Implementation",
        "Stand up Jobpac the <em>right way</em> the first time.",
        "For a successful rollout of software you need the 3 P&rsquo;s &mdash; <strong>People / Product / Processes.</strong> We project manage representing you while the vendor implements the core system, so you get the best out of your investment. We will demonstrate various ways you can use it, so we get the right way for your business.",
        image_src="consultant-on-site.jpg",
        image_alt="Construction supervisor reviewing project data on an iPad on site",
        badge="On site &middot; Sydney",
        float_stat={"num": "11 wks", "lbl": "avg go-live"},
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">What we do</span>
          <h2>What an implementation looks like <em>with us</em>.</h2>
          <p class="lead">We perform an <strong>AS IS</strong> and <strong>TO BE</strong> scope so you can see what it&rsquo;s going to look like when implemented.<br/>We ask you to select a small group of your &ldquo;power users&rdquo; to be part of the Jobpac rollout &mdash; CFO, CM, PMs, CAs.<br/>Getting the processes locked away and signed off by your key team members is the key to a successful rollout.<br/>Our focus is representing <em>you</em> the whole way through the Jobpac implementation.</p>
        </div>
        <ul class="deliverables-strip reveal">
          <li><strong>Greenfield rollouts</strong>From an empty system to a fully-configured live environment in 8&ndash;14 weeks.</li>
          <li><strong>ERP migrations</strong>Coming off MYOB, Xero, Reckon, or a legacy purpose-built system &mdash; we plan the transition without losing project data integrity.</li>
          <li><strong>Module-by-module deployments</strong>Already running parts of Jobpac and adding more? We'll roll out additional modules in your live system without disrupting day-to-day.</li>
          <li><strong>Data migration &amp; validation</strong>Project history, supplier records, contract values, retentions held &mdash; mapped, migrated, reconciled.</li>
          <li><strong>Post go-live stabilisation</strong>The first month-end after go-live is where most projects die. We're there for that one. And the next one.</li>
        </ul>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Implementation phases</span>
          <h2>Five-phase delivery, fixed scope.</h2>
          <p class="lead">Every implementation moves through the same five phases. We design backwards from go-live, not forwards from a vendor template.</p>
        </div>
        <div class="feature-grid five-up">
          <div class="feature-card reveal">
            <div class="num">Phase 01</div>
            <h3>Discovery</h3>
            <p>We sit with your finance lead, project managers, and ops team. We map your current state &mdash; not a generic ERP-vendor questionnaire. By the end of week one, we know what success looks like on day one after go-live.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">Phase 02</div>
            <h3>Design</h3>
            <p>Project structure, chart of accounts, cost code library, claim workflows, approval chains, integration points. All documented in writing before we touch the system. You sign off on the design before any build starts.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">Phase 03</div>
            <h3>Build</h3>
            <p>Configuration, integrations, data migration. Your team sees a working sandbox at week six, not week twelve. You can poke at it and break it without consequence &mdash; we'd rather find the issues there than in production.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">Phase 04</div>
            <h3>Train &amp; cutover</h3>
            <p>Role-based training for the people who'll actually use it &mdash; PMs, AP/AR, payroll, finance leadership. Then a planned cutover with a documented rollback path. Not a &ldquo;fingers crossed&rdquo; weekend.</p>
          </div>
          <div class="feature-card reveal">
            <div class="num">Phase 05</div>
            <h3>Stabilise</h3>
            <p>We're embedded for the first month-end and the first project claim cycle. By the time we step back, your team owns it &mdash; with the documentation and the muscle memory to keep it running.</p>
          </div>
          <div class="phase-outcome reveal" aria-hidden="true">
            <div class="po-head">
              <span class="po-live"><span class="pulse"></span>Live</span>
              <div class="po-dots"><span></span><span></span><span></span></div>
            </div>
            <div class="po-title">Day 1 after go-live</div>
            <div class="po-stat">
              <span class="po-num">11<span class="po-unit">wks</span></span>
              <span class="po-sublabel">kick-off &rarr; go-live</span>
            </div>
            <svg class="po-spark" viewBox="0 0 200 60" preserveAspectRatio="none">
              <defs>
                <linearGradient id="spark-grad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="currentColor" stop-opacity="0.35"/>
                  <stop offset="100%" stop-color="currentColor" stop-opacity="0"/>
                </linearGradient>
              </defs>
              <polyline points="0,55 30,50 60,42 90,38 120,28 150,20 180,14 200,8 200,60 0,60" fill="url(#spark-grad)"/>
              <polyline points="0,55 30,50 60,42 90,38 120,28 150,20 180,14 200,8" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/>
              <circle cx="200" cy="8" r="4" fill="currentColor"/>
              <circle cx="200" cy="8" r="8" fill="currentColor" fill-opacity="0.3"/>
            </svg>
            <div class="po-checks">
              <span>Finance + payroll + projects live</span>
              <span>Team trained, owns it</span>
            </div>
          </div>
        </div>
      </div>
    </section>

""" + process_section() + """

""" + testimonial_section(
        "Buoy stood up Jobpac for us in <em>11 weeks</em> and stuck around for the first three month-ends. By the time they left, our finance team owned the system in a way they never owned the old one.",
        "OD", "Operations Director", "Tier-2 commercial builder &middot; Sydney",
        portrait_src="client-portrait.jpg",
        portrait_alt="Operations Director portrait",
    ) + """

""" + stats_section(
        "By the numbers",
        "Implementation, the way we run it.",
        [
            ("8&ndash;14 wks", "typical timeline from kick-off to go-live"),
            ("40+", "Jobpac implementations delivered across AU/NZ"),
            ("100%", "senior consultants &mdash; no juniors or graduates"),
            ("Fixed", "scope and price, signed off before build starts"),
        ],
    ) + """

""" + faq_section([
        ("How long does a typical Jobpac implementation take?",
         "For a single-entity construction business with standard modules, eight to ten weeks from kick-off to go-live is typical. Multi-entity rollouts, complex integrations, or businesses migrating data from an older system usually run twelve to fourteen weeks. We give you the timeline in the proposal &mdash; not a &ldquo;roughly three months&rdquo; handwave."),
        ("What if we're already running another ERP &mdash; can you migrate us?",
         "Yes. We've migrated clients off MYOB, Xero, Reckon, Cheops, and various legacy systems built in-house. The work is in mapping project structure and historical data so nothing critical gets lost. We do that as a defined work-stream inside the implementation, not as a hand-wave."),
        ("Do you handle the data migration ourselves, or do we?",
         "We lead the data migration but we don't do it in a black box. Your team validates the migrated data at every stage &mdash; opening balances, project budgets, retentions held, AR/AP open items. Nothing goes live until you've signed off."),
        ("What happens after go-live?",
         "We're embedded for the first month-end and the first full project claim cycle after go-live &mdash; that's where most implementations die. After that, you can hand back to your team entirely, or move to a same-day support arrangement. Most clients do a 60- or 90-day support runway, then step back."),
        ("Can we phase this in module by module?",
         "Yes. If you want to go live on core financials first and add payroll, plant, and forecasting later, that's a fine sequence. We'll plan the phasing so each module's go-live is stable before the next one starts. Phase 2 doesn't get quoted in vague terms &mdash; we treat it as its own fixed-scope engagement."),
        ("Who actually does the work &mdash; a senior or a graduate?",
         "A senior consultant. Always. The person you meet in discovery is the person doing the build, configuration, and training. We don't have graduates on the bench &mdash; partly because we're not big enough, but mostly because we don't want to."),
    ]) + """

""" + cta_big(
        eyebrow="Ready when you are",
        headline_html="Planning a Jobpac <em>rollout</em> or migration?",
        lead="Get a fixed-scope proposal within a week. Senior consultant on the call, no junior intermediary. We'll tell you what's likely fixable, what isn't, and what we'd do first.",
        features=[
            "Fixed-scope, fixed-price proposal in writing",
            "Named senior consultant from day one",
            "30-minute call. No slide deck. No obligation.",
        ],
        stat_num_html='11<span class="cta-big-stat-unit">wks</span>',
        stat_label="average Jobpac go-live with Buoy",
    ),
)

# -------- Process Improvement --------
PAGES["process-improvement.html"] = dict(
    title="Process Improvement",
    description="Jobpac process audit, workflow rebuild, and configuration improvement for construction businesses already using Jobpac. Get the value you paid for.",
    active="services",
    body=hero_with_visual(
        "Process Improvement",
        "You bought the software. We make sure you <em>actually</em> get value from it.",
        "Most Jobpac users we meet have the system &mdash; they just aren't getting the most out of it. The system hasn&rsquo;t been looked at since it was implemented and workarounds in spreadsheets do the work the system was meant to do. We audit how Jobpac is actually being used, find the gaps, and rebuild the workflows around how your team really works.",
        image_src="process-audit.jpg",
        image_alt="Senior consultant reviewing project finance data with a client",
        badge="Audit in progress",
        float_stat={"num": "17", "lbl": "avg findings per audit"},
    ) + """
    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Where we look</span>
          <h2>Where we usually find the leaks.</h2>
          <p class="lead">After sixteen years inside Jobpac across hundreds of construction businesses, the gaps cluster in predictable places. The audit tells us which ones are yours.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal"><div class="num">Underused modules</div><h3>Modules switched off.</h3><p>You're paying for plant, or the BFM that are no longer used or aren't being used as intended.</p></div>
          <div class="feature-card reveal"><div class="num">Manual workarounds</div><h3>Excel doing system work.</h3><p>Critical information is being controlled in spreadsheets because the users have gone maverick on you or people have left the business and Jobpac processes have fallen away or configuration changes haven&rsquo;t been looked at.</p></div>
          <div class="feature-card reveal"><div class="num">Reporting gaps</div><h3>Days to compile a P&amp;L.</h3><p>Project Reporting is critical to controlling your costs and WIP versus CWIP. When we have established that, we can then forecast our costs that haven&rsquo;t been committed. If it isn&rsquo;t in Jobpac, it doesn&rsquo;t exist.</p></div>
          <div class="feature-card reveal"><div class="num">Approval chaos</div><h3>Around the system, not through.</h3><p>Invoices are not being connected to POs in the system? Users are sending PO&rsquo;s outside of the system instead of through it? Audit trail is patchy and impossible to defend.</p></div>
          <div class="feature-card reveal"><div class="num">Stale configuration</div><h3>Five-year-old chart of accounts.</h3><p>Cost code library or chart of accounts hasn't been touched in years and is no longer a good fit for your project job costing.</p></div>
          <div class="feature-card reveal"><div class="num">Training debt</div><h3>People inventing workflows.</h3><p>People hired post-implementation never got proper training and have invented their own way of doing things.</p></div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">How it runs</span>
          <h2>How an audit actually runs.</h2>
          <p class="lead">A senior consultant spends two to three days inside your business. We sit with the people doing the work, not just the executives. We watch a real claim cycle, a real month-end, a real project setup. You get a written audit at the end &mdash; ranked findings, remediation effort, expected payback.</p>
        </div>
        <div class="outcomes reveal" style="margin-top: 2rem;">
          <div class="o"><span class="num">2 hours</span><span class="lbl">system parameter &amp; menu audits</span></div>
          <div class="o"><span class="num">12&ndash;20</span><span class="lbl">findings ranked by effort to fix and expected payback</span></div>
          <div class="o"><span class="num">Fixed</span><span class="lbl">scope and price &mdash; no T&amp;E surprises</span></div>
        </div>
      </div>
    </section>

    <section class="section bfm-callout reveal">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">What we cover</span>
          <h2>Business Forecasting Module &mdash; <em>inside Jobpac</em>, not next to it.</h2>
        </div>
        <ul class="bfm-tags reveal">
          <li>Accruals</li>
          <li>Forecasting</li>
          <li>Risk &amp; Opportunities</li>
          <li>Revenue to Project Turnover</li>
          <li>WIP v CWIP</li>
          <li>WIH</li>
          <li>Cashflow</li>
          <li>Variations</li>
        </ul>
      </div>
    </section>

""" + process_section() + """

""" + testimonial_section(
        "We thought we knew where the inefficiencies were. After two days, Buoy gave us a list of <em>seventeen ranked findings</em> &mdash; the first three paid back in the first quarter.",
        "FD", "Finance Director", "Civil contractor &middot; Brisbane",
        portrait_src="portrait-cfo.jpg",
        portrait_alt="Finance Director portrait",
    ) + """

""" + stats_section(
        "By the numbers",
        "What an audit actually delivers.",
        [
            ("2 hours", "system parameter &amp; menu audits"),
            ("12&ndash;20", "ranked findings per audit, with effort and payback estimates"),
            ("Q1", "typical payback period on the first wave of fixes"),
            ("Fixed", "audit fee &mdash; no T&amp;E surprises"),
        ],
    ) + """

""" + faq_section([
        ("How does the audit actually work?",
         "A senior consultant spends two to three days inside your business &mdash; not in a meeting room reading slide decks, but sitting with the people doing the work. We watch a real claim cycle, a real month-end, a real project setup. At the end you get a written audit with twelve to twenty findings, each ranked by effort to fix and expected payback."),
        ("Do you fix the issues yourselves, or just identify them?",
         "Either. The audit is the same price whether you take the findings and execute them in-house, or hand the remediation back to us. We're equally happy doing the remediation work or coaching your team through it. Most clients fix the highest-payback items with us and tackle the rest themselves."),
        ("What does an audit typically cost?",
         "Audits are based on the size of the business. We provide you a quote so no surprises."),
        ("We think we already know what's broken &mdash; is the audit still worth it?",
         "Usually yes. After sixteen years of doing this, the patterns are predictable &mdash; but the specific findings inside your business almost always include things the people running the system every day no longer see. We've never finished an audit without surfacing material issues the client didn't know about."),
        ("Will this disrupt our finance team's day-to-day?",
         "Minimally. The audit runs alongside normal operations. We need to watch the work happening &mdash; not interrupt it. People feel observed for a day or two, but the audit doesn't stop anyone from doing their job."),
        ("Is this only for businesses already running Jobpac?",
         "Yes. Process improvement assumes you have the system installed and being used. If you're considering Jobpac but not yet on it, you want the implementation conversation instead."),
    ]) + """

""" + cta_big(
        eyebrow="Most audits pay back in a quarter",
        headline_html="Suspect Jobpac isn't <em>pulling</em> its weight?",
        lead="Most of the value an audit unlocks is paid back in the first quarter. Tell us where it hurts — we'll come back with a fixed-price proposal within a week.",
        features=[
            "Two to three days on-site, fixed-price audit",
            "Twelve to twenty findings, ranked by payback",
            "Remediation on your terms &mdash; in-house or with us",
        ],
        stat_num_html='Q1',
        stat_label="typical payback period on the audit",
        badge_text="Senior consultant on the audit",
    ) + """""",
)

# -------- Support (parent) --------
PAGES["support.html"] = dict(
    title="Support",
    description="Same-day Jobpac support, plus ongoing finance and accounting cover for construction businesses: bookkeeping, AP/AR, payroll, P&L, temp relief, and forecasting.",
    active="services",
    body=hero_with_visual(
        "Support",
        "Your finance team's safety net &mdash; answered the <em>same day</em>, every day.",
        "Buoy's support service is what construction finance teams reach for when the wheels need to keep turning. Day-to-day Jobpac help, real human bookkeeping and accounting cover, and temp relief when someone's sick or away. On-call or fully embedded &mdash; the cost of an in-house resource without the cost of a permanent hire.",
        image_src="office-team.jpg",
        image_alt="Buoy support consultants working at desk with project dashboards",
        banner="Same-day support &mdash; usually answered within hours.",
        badge="Live &middot; Mon&ndash;Fri AU/NZ",
        float_stat={"num": "&lt;4hrs", "lbl": "avg resolution time"},
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="reveal">
          <span class="eyebrow">Inside Support</span>
          <h2>Seven specialist disciplines, one team.</h2>
          <p class="lead">Pick the bits you need. Most clients start with one or two and expand as they see the value.</p>
        </div>
        <div class="sub-grid">
          <a href="support-bookkeeping.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">BK</div>
            <h3>Bookkeeping</h3>
            <p>Day-to-day Jobpac bookkeeping, monthly close, reconciliations, and BAS-ready books.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-accounts-payable.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">AP</div>
            <h3>Accounts Payable</h3>
            <p>Subbie claims, RCTI generation, vendor management, and clean payment runs in Jobpac.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-accounts-receivable.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">AR</div>
            <h3>Accounts Receivable</h3>
            <p>Progress claims, customer invoicing, retention tracking, and collection of overdue accounts.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-payroll.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">PR</div>
            <h3>Payroll</h3>
            <p>Award- and EBA-compliant payroll, super, STP reporting, and timesheet integration.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-profit-loss.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">P&amp;L</div>
            <h3>Profit &amp; Loss</h3>
            <p>Project- and entity-level P&amp;L, monthly management reporting, and forecast-vs-actual analysis.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-temp-relief.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">TR</div>
            <h3>Temp Relief</h3>
            <p>Short-term cover for sick leave, parental leave, holidays, or peak-period workload.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
          <a href="support-business-forecasting.html" class="sub-card reveal" style="text-decoration:none;color:inherit;">
            <div class="icon">FC</div>
            <h3>Business Forecasting</h3>
            <p>Integrated revenue, cash, and project pipeline forecasts &mdash; built and maintained in Jobpac.</p>
            <span class="more">Learn more <span class="arr">→</span></span>
          </a>
        </div>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">How it actually works</span>
          <h2>Same day. <em>Senior.</em> No triage queue.</h2>
          <p class="lead">You email or call. A senior consultant who knows your setup picks it up directly &mdash; not a triage queue, not an offshore ticket centre. The context compounds month after month, so we're faster every time.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal"><div class="num">Same day</div><h3>Response on every business day</h3><p>No 48-hour SLA, no &ldquo;next business day.&rdquo; A senior with full context picks up directly.</p></div>
          <div class="feature-card reveal"><div class="num">&lt; 4 hrs</div><h3>Average resolution</h3><p>Most queries are resolved within a couple of hours. Same business day at the latest.</p></div>
          <div class="feature-card reveal"><div class="num">No queue</div><h3>A senior on the keys</h3><p>The same person works your account month after month. We're not re-discovering your environment every time.</p></div>
          <div class="feature-card reveal"><div class="num">AU &amp; NZ</div><h3>Business hours coverage</h3><p>Mon-Fri across both timezones. Out-of-hours and EOFY cover by arrangement.</p></div>
        </div>
      </div>
    </section>

""" + process_section() + """

""" + testimonial_section(
        "The same-day support claim is real. We've had questions answered <em>within 90 minutes</em> from a senior who actually understands how Jobpac handles retentions. Magnitude better than a 48-hour ticket SLA.",
        "FM", "Finance Manager", "Multi-entity construction group &middot; Melbourne",
        portrait_src="portrait-finance-manager.jpg",
        portrait_alt="Finance Manager portrait",
    ) + """

""" + faq_section([
        ("How fast is 'same-day support' really?",
         "Most tickets are answered within two to three hours of you sending them, often faster. The same business day at the absolute latest. No triage queue &mdash; the senior consultant who knows your setup picks it up directly. The only exception is genuinely complex work that needs a few days of focused effort, in which case we tell you up front."),
        ("Is there a minimum commitment?",
         "No. You can use Buoy support ad-hoc (pay for what you use), on a project basis (a defined chunk of work), or on a retainer (set hours per month). Most clients start ad-hoc, then move to a retainer once they realise they're reaching for us every week anyway."),
        ("Do you work weekends or after hours?",
         "Standard support runs AU/NZ business hours. For known go-live weekends, EOFY closes, or other planned out-of-hours work, we'll cover by arrangement &mdash; agreed in advance, scoped explicitly. We don't do midnight pager duty."),
        ("Can you cover for someone on long-term leave?",
         "Yes &mdash; this is one of the most common reasons clients reach for us. Parental leave, long-service leave, an unexpected resignation: we can put a senior into the seat by the start of next week. Day one productivity, not week three."),
        ("Do you replace our in-house finance team?",
         "No, and we don't try to. Our goal is to make your in-house team faster, more accurate, and less reliant on heroics &mdash; not to displace them. When we leave, you should be better at running Jobpac than when we arrived."),
        ("How quickly can a new support arrangement start?",
         "For most clients, same week. Discovery call Tuesday, scope agreed Thursday, working in your system Monday. If you're in genuine &ldquo;wheels about to fall off&rdquo; territory, tell us &mdash; we'll work out what's possible faster."),
    ]) + """

""" + cta_big(
        eyebrow="We can start this week",
        headline_html="Need a finance hand &mdash; <em>today</em>?",
        lead="Tell us what's going sideways. If we can help, we'll start same week. If we can't, we'll say. The first conversation is free.",
        features=[
            "Same-day response, every business day",
            "No triage queue &mdash; a senior picks up directly",
            "Ad-hoc, project, or ongoing retainer &mdash; your call",
        ],
        stat_num_html="Same day",
        stat_label="every business day, no triage queue",
        badge_text="Senior consultant ready",
    ),
)

# -------- Training --------
PAGES["training.html"] = dict(
    title="Training",
    description="Hands-on Jobpac training for construction and civil teams, tailored to your modules, your team's experience level, and your real project workflows.",
    active="services",
    body=hero_with_visual(
        "Training",
        "Hands&#8209;on Jobpac training tailored to <em>your team</em>.",
        "Generic Jobpac training videos are easy to find. Training tailored to your modules, your project structure, and your team's actual experience level isn't. We deliver training that's grounded in your real Jobpac environment &mdash; not a clean demo system that looks nothing like yours.",
        image_src="training-session.jpg",
        image_alt="Buoy trainer delivering a Jobpac workshop to a construction finance team",
        badge="Workshop &middot; In session",
        float_stat={"num": "Real", "lbl": "training on your live Jobpac"},
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="two-col reveal">
          <div>
            <h2>Built for your team, not the textbook.</h2>
            <p>Every training engagement starts with a 30-minute call to understand who's in the room. New starters who've never seen Jobpac? Long-timers picking up new modules? PMs who only need to read reports?</p>
            <p>We design the syllabus from there. Sessions run on a sandbox of your real Jobpac environment, with your project structure and cost codes &mdash; so what people learn is what they'll actually do on Monday.</p>
          </div>
          <div>
            <h2>Formats we run.</h2>
            <ul class="deliverables">
              <li><strong>On-site workshops</strong>Half-day or full-day sessions at your office, with a senior consultant in the room.</li>
              <li><strong>Remote sessions</strong>Live, interactive, screen-shared. Recorded so the team can rewatch.</li>
              <li><strong>Role-specific tracks</strong>Project managers, accounts payable, payroll, finance leadership &mdash; each gets training calibrated to what they touch.</li>
              <li><strong>New-starter packs</strong>A fixed onboarding programme so the next hire doesn't take three months to come up to speed.</li>
              <li><strong>Recorded library</strong>We'll record the sessions and hand you a private library your team can reference long after we leave.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Module coverage</span>
          <h2>What we train on.</h2>
          <p class="lead">Every Jobpac module, calibrated to the modules you've actually licensed and the roles in your team that use them.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal"><div class="num">Core</div><h3>Project setup &amp; structure</h3><p>Job creation, cost code mapping, budget loading, contract values, variations, retentions. The foundation everything else builds on.</p></div>
          <div class="feature-card reveal"><div class="num">Finance</div><h3>AP / AR / GL</h3><p>Subbie claims, vendor invoices, customer billing, period close, GL reconciliation, monthly close discipline.</p></div>
          <div class="feature-card reveal"><div class="num">Payroll</div><h3>Payroll &amp; timesheets</h3><p>Weekly and monthly cycles, award rates, EBA configuration, STP Phase 2, super, leave administration, timesheet integration.</p></div>
          <div class="feature-card reveal"><div class="num">Reporting</div><h3>Reports &amp; dashboards</h3><p>Project P&amp;L, forecast-vs-actual, cashflow, custom reports, exporting and pivoting for management packs.</p></div>
          <div class="feature-card reveal"><div class="num">Plant</div><h3>Plant &amp; equipment</h3><p>Plant ledger, internal hire rates, plant cost recovery to projects, idle-time tracking, replacement planning.</p></div>
          <div class="feature-card reveal"><div class="num">Forecast</div><h3>Forecasting &amp; cashflow</h3><p>Building and maintaining live project and entity forecasts inside Jobpac &mdash; not in a parallel spreadsheet that goes stale.</p></div>
        </div>
      </div>
    </section>

""" + process_section() + """

""" + testimonial_section(
        "Our team had been on Jobpac for three years and was still using it like an expensive spreadsheet. <em>Three days of training</em> with our real data and project structure, and monthly reporting changed overnight.",
        "FL", "Finance Lead", "Fit-out specialist &middot; Auckland",
        portrait_src="portrait-finance-lead.jpg",
        portrait_alt="Finance Lead portrait",
    ) + """

""" + stats_section(
        "By the numbers",
        "Training that earns its keep.",
        [
            ("Role-based", "tracks for PMs, AP/AR, payroll, finance leadership"),
            ("Sandbox", "of your live Jobpac environment, not a demo system"),
            ("On-site or", "remote &mdash; your choice, including hybrid"),
            ("Recorded", "library handed over, plus written reference guides"),
        ],
    ) + """

""" + faq_section([
        ("How do you tailor training to our specific team?",
         "Every training engagement starts with a 30-minute scoping call to understand who's in the room: experience level, modules they actually touch, and what they're struggling with today. The syllabus is designed from there. Sessions run on a sandbox of your real Jobpac &mdash; same project structure, same cost codes, same workflows."),
        ("Do you deliver on-site or remote?",
         "Both. On-site workshops work best for hands-on modules and team-wide training days. Remote sessions are good for refreshers, smaller groups, or distributed teams. Many clients do a hybrid: kick-off and major modules on-site, follow-ups remote."),
        ("Can you train new starters joining our business?",
         "Yes &mdash; we have a fixed onboarding programme for new finance hires that runs three to five sessions over their first month. By the end of it, they should be able to do their job in Jobpac without senior hand-holding. Much faster than the usual &ldquo;watch and learn&rdquo; approach."),
        ("What if my team is at very different experience levels?",
         "We split the training. A long-standing payroll officer doesn't need to sit through &ldquo;this is how you log in&rdquo;; a new starter doesn't need an advanced reporting session in their first week. We design tracks by role and level, run in parallel or sequence."),
        ("Do you record the sessions?",
         "Yes, by default. We hand over a private library of recordings your team can reference long after we leave. Most clients also ask for written reference guides covering the specific workflows in their setup &mdash; we include those too."),
        ("Can we train on a sandbox, or does it have to be our live Jobpac?",
         "We default to a sandbox copy of your live system. People are more willing to experiment when they can't break production. For some advanced sessions where the sandbox can't realistically replicate the workflow (heavy reporting, integration testing), we'll work in production with read-only or test-account access."),
    ]) + """

""" + cta_big(
        eyebrow="Built for your real team",
        headline_html="Got a team that needs to <em>level up</em> on Jobpac?",
        lead="Send us the headcount and the modules. We come back with a tailored syllabus and a fixed price, ready to deliver on-site or remote.",
        features=[
            "Tailored to your modules and project structure",
            "On-site, remote, or hybrid &mdash; your call",
            "Recorded library handed over after every session",
        ],
        stat_num_html="Real",
        stat_label="training on your live Jobpac, not a demo",
        badge_text="Senior trainer delivering",
    ),
)

# -------- Civil & Construction --------
PAGES["civil-construction.html"] = dict(
    title="Civil & Construction",
    description="Specialist Jobpac focus on civil and commercial construction: subbie claims, retentions, progress billing, plant costing, and stage claims.",
    active="services",
    body=hero_with_visual(
        "Civil &amp; Construction",
        "Specialist focus on the <em>unique mechanics</em> of civil and commercial construction.",
        "Jobpac was built for construction and we built our consultancy for the same audience. We know subbie claims, retentions, plant costing, stage billing, and JV multi-entity reporting from inside the businesses that run them &mdash; not from a vendor's marketing deck.",
        image_src="civil-works.jpg",
        image_alt="Civil construction site managers reviewing plans on a tablet during infrastructure works",
        badge="On site &middot; Civil",
        float_stat={"num": "16", "lbl": "years specialising"},
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="two-col reveal">
          <div>
            <h2>Where industry knowledge changes the answer.</h2>
            <p>Most ERP consultants will configure what you ask for. We'll tell you what you should be asking for, because we know the operational realities the configuration has to survive.</p>
            <p>That shows up in retention treatment, progress claim formats, head-contract vs subcontract billing logic, plant cost-recovery models, and how a JV reports back to its parents. The differences are small in isolation. They compound across a year of project closeouts.</p>
          </div>
          <div>
            <ul class="deliverables">
              <li><strong>Subbie claim processing</strong>RCTI generation, retention release tracking, statutory declarations, payment claim/payment schedule timing under the Security of Payment Acts.</li>
              <li><strong>Retentions, ledger to ledger</strong>Tracked correctly on both sides &mdash; what you owe subbies and what's withheld from you by the head contractor.</li>
              <li><strong>Progress billing</strong>Stage claims, schedule of values, milestone billing, and reconciliation against the head contract.</li>
              <li><strong>Plant &amp; equipment costing</strong>Internal hire rates, plant ledger maintenance, cost recovery to projects, idle-time tracking.</li>
              <li><strong>Multi-entity / JV structures</strong>Inter-entity charges, JV reporting back to parent entities, consolidated and standalone P&amp;L.</li>
              <li><strong>Variations &amp; contract value tracking</strong>Approved variations vs pending vs disputed &mdash; visible at the project line, not buried in spreadsheets.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Who we work with</span>
          <h2>The businesses we know best.</h2>
          <p class="lead">Most of our clients fit one of these profiles. If yours doesn't, the conversation might still be worth having.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal"><div class="num">Tier 2</div><h3>Tier-2 commercial builders</h3><p>$50m&ndash;$500m turnover, multiple concurrent projects, growing pains around forecast accuracy and project-level margin visibility.</p></div>
          <div class="feature-card reveal"><div class="num">Civil</div><h3>Civil contractors</h3><p>Roads, bridges, utilities, earthworks. Heavy plant, day-rate hire, stage-based billing, complex retention release timing.</p></div>
          <div class="feature-card reveal"><div class="num">Fit-out</div><h3>Fit-out &amp; refurb specialists</h3><p>Fast turn-over jobs, high subbie density, tight margin discipline, lots of variations and partial claims to track.</p></div>
          <div class="feature-card reveal"><div class="num">Family</div><h3>Family-owned regional builders</h3><p>Decades of operating know-how, leaner finance teams, modernising off legacy systems or spreadsheet-driven processes.</p></div>
          <div class="feature-card reveal"><div class="num">JV</div><h3>Joint ventures &amp; alliances</h3><p>Multi-entity reporting back to parent companies, inter-entity charges, consolidated and standalone P&amp;L for each partner.</p></div>
          <div class="feature-card reveal"><div class="num">Group</div><h3>Multi-entity construction groups</h3><p>Holding company structures with operating subsidiaries, intercompany trading, consolidated reporting, separate ABNs.</p></div>
        </div>
      </div>
    </section>

""" + process_section() + """

""" + testimonial_section(
        "They speak the language. When we discussed retention treatment, they didn't need the construction-finance crash course &mdash; they came with the answer. <em>Sixteen years</em> in this industry shows up in every conversation.",
        "MD", "Managing Director", "Family-owned civil contractor &middot; Regional NSW",
        portrait_src="portrait-md.jpg",
        portrait_alt="Managing Director portrait",
    ) + """

""" + stats_section(
        "By the numbers",
        "Why specialism matters.",
        [
            ("16", "years specialising in construction &amp; civil &mdash; only"),
            ("$20m&ndash;$500m", "typical client turnover range"),
            ("AU &amp; NZ", "on-site from Sydney, Melbourne, Brisbane, Auckland"),
            ("100+", "combined years of construction-industry experience"),
        ],
    ) + """

""" + faq_section([
        ("Do you only work with civil contractors, or commercial builders too?",
         "Both. The mechanics overlap heavily &mdash; subbie claims, retentions, progress billing, project-level P&amp;L, plant costing are common across civil and commercial. The specifics differ (more plant in civil, more variations in fit-out) but the consultant skill is the same."),
        ("What size of business do you typically work with?",
         "Most clients are between $20m and $500m turnover &mdash; mid-market construction businesses with one finance function. Smaller and we're usually overkill. Larger and there's typically an internal team that needs different kinds of help. Either way, the discovery call tells us quickly."),
        ("Do you handle JV / multi-entity reporting?",
         "Yes &mdash; it's one of our specialty areas. Joint ventures, parent-subsidiary reporting, inter-entity charges, consolidated and standalone P&amp;L. Most ERP consultancies hand-wave this; we've configured it dozens of times and know where the edge cases live."),
        ("Are you familiar with Security of Payment Act timing for claims?",
         "Yes. Payment claim service dates, payment schedule response windows, statutory declarations, the lot. We configure Jobpac so the system supports the legal requirements rather than fighting them &mdash; including the differences between NSW, Vic, Qld, WA, and NZ regimes."),
        ("Do you work with regional businesses outside the capital cities?",
         "Yes. We're based in Sydney, Melbourne, Brisbane, and Auckland, and we travel anywhere in AU/NZ for on-site work. Regional family-owned builders are some of our favourite clients &mdash; deeply experienced operators modernising legacy finance functions."),
        ("Can you help with plant cost recovery and internal hire rates?",
         "Yes. Plant ledger setup, internal hire rate cards, recovery to projects, idle-time tracking, replacement-cost analysis. It's one of the most under-used parts of Jobpac at most civil contractors we audit &mdash; the configuration is usually the bottleneck, not the software."),
    ]) + """

""" + cta_big(
        eyebrow="Construction-native since 2010",
        headline_html="Want a Jobpac partner who <em>actually</em> knows civil?",
        lead="Most consultancies will service any ERP and any sector. We do one ERP, in one industry, and we've done it for sixteen years. Tell us about your business.",
        features=[
            "Construction &amp; civil &mdash; only",
            "Subbie claims, retentions, plant costing, JV reporting",
            "On-site from Sydney, Melbourne, Brisbane, Auckland",
        ],
        stat_num_html='16<span class="cta-big-stat-unit">yrs</span>',
        stat_label="specialising in construction &amp; civil",
        badge_text="Industry specialist on the call",
    ),
)

# -------- Contact --------
PAGES["contact.html"] = dict(
    title="Contact",
    description="Get in touch with Buoy Consulting. Same-day responses on weekdays. Specialist Jobpac help for construction and civil businesses across Australia and New Zealand.",
    active="contact",
    body=page_hero(
        "Get in touch",
        "Tell us what's stuck. We'll come back the <em>same day</em>.",
        "Send an email or pick up the phone &mdash; whichever you prefer. A senior consultant reads everything that comes in. We respond on the same business day, usually within a couple of hours.",
        banner="Same-day responses on AU/NZ business days.",
        center=True,
    ) + """
    <section class="section">
      <div class="wrap">
        <div class="outcomes reveal">
          <div class="o"><span class="num">Same day</span><span class="lbl">response on every business day, no triage queue</span></div>
          <div class="o"><span class="num">&lt;4hrs</span><span class="lbl">average response time &mdash; often less</span></div>
          <div class="o"><span class="num">Senior</span><span class="lbl">consultant reads everything that comes in</span></div>
        </div>
      </div>
    </section>

    <section class="section warm-bg-rich">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Get in touch</span>
          <h2>Talk to a <em>senior</em>, not a routing desk.</h2>
          <p class="lead">Whichever channel you use, you'll reach a senior consultant who can actually answer the question. We don't queue and we don't triage.</p>
        </div>
        <div class="contact-channels reveal">
          <a href="mailto:info@buoyconsultancy.com.au" class="contact-channel-card">
            <span class="cc-icon" aria-hidden="true">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            </span>
            <span class="cc-label">Email us</span>
            <span class="cc-handle">info@buoyconsultancy.com.au</span>
            <span class="cc-meta">Direct to the team. Same-day reply on business days.</span>
          </a>
          <a href="tel:+61292345678" class="contact-channel-card">
            <span class="cc-icon" aria-hidden="true">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            </span>
            <span class="cc-label">Sydney HQ</span>
            <span class="cc-handle">+61 2 9234 5678</span>
            <span class="cc-meta">Mon&ndash;Fri, 8am to 6pm AEST. Senior consultant on the line.</span>
          </a>
          <a href="tel:+6498883333" class="contact-channel-card">
            <span class="cc-icon" aria-hidden="true">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            </span>
            <span class="cc-label">NZ direct line</span>
            <span class="cc-handle">+64 9 888 3333</span>
            <span class="cc-meta">Mon&ndash;Fri, 9am to 5:30pm NZST. Direct to the Auckland team.</span>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">What happens next</span>
          <h2>The path from here to a call.</h2>
          <p class="lead">Three short steps. No slide deck, no forms in the way, no obligation at any stage.</p>
        </div>
        <div class="next-steps-grid reveal">
          <div class="next-step-card">
            <span class="step-num">01</span>
            <h3>Same-day reply</h3>
            <p>From a senior consultant, on every business day. Often within a couple of hours. No triage queue, no offshore ticket centre.</p>
          </div>
          <div class="next-step-card">
            <span class="step-num">02</span>
            <h3>Discovery call</h3>
            <p>30 minutes, no slide deck, no obligation &mdash; if we're a fit. You'll be talking to the senior who'd do the work, not a sales person.</p>
          </div>
          <div class="next-step-card">
            <span class="step-num">03</span>
            <h3>Or a referral</h3>
            <p>If we're not the right partner for what you need, we'll tell you straight &mdash; and point you at someone who is. Either way you get value from the call.</p>
          </div>
        </div>
      </div>
    </section>""",
)

# -------- Support sub-pages --------
def support_subpage(slug, title, code, h1, lead, blurb, deliverables, focus_h, focus_items):
    body = hero_with_visual(
        f"Support &mdash; {title}",
        h1,
        lead,
        image_src="office-team.jpg",
        image_alt="Buoy support consultants at work with construction finance teams",
        banner="Same-day support, every day",
        badge="Live &middot; Mon&ndash;Fri AU/NZ",
        float_stat={"num": "&lt;4hrs", "lbl": "avg resolution time"},
    ) + f"""
    <section class="section">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">What we cover</span>
          <h2>{title} support, <em>end&#8209;to&#8209;end</em>.</h2>
          <p class="lead">{blurb}</p>
        </div>
        <ul class="deliverables-strip reveal">
          {''.join(f'<li><strong>{d[0]}</strong>{d[1]}</li>' for d in deliverables)}
        </ul>
      </div>
    </section>

    <section class="section dark-feature">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">Why teams choose us</span>
          <h2>Same day. <em>Senior.</em> No queue.</h2>
          <p class="lead">When you hire Buoy for {title.lower()} cover, this is what you actually get &mdash; not a 48-hour SLA and an offshore ticket queue.</p>
        </div>
        <div class="feature-grid">
          <div class="feature-card reveal"><div class="num">Same day</div><h3>Response on every business day</h3><p>No triage queue, no &ldquo;next business day.&rdquo; A senior who knows your setup picks up directly.</p></div>
          <div class="feature-card reveal"><div class="num">&lt; 4 hrs</div><h3>Average resolution time</h3><p>Most queries are closed within hours of you sending them, often faster &mdash; same business day at the latest.</p></div>
          <div class="feature-card reveal"><div class="num">Senior</div><h3>Consultant on every job</h3><p>No graduates, no juniors. The person on the keys has spent years inside Jobpac in construction businesses.</p></div>
        </div>
      </div>
    </section>

    <section class="section warm-bg-rich">
      <div class="wrap">
        <div class="section-head reveal">
          <span class="eyebrow">How we work</span>
          <h2>{focus_h}</h2>
        </div>
        <ul class="checklist reveal" style="max-width: 760px; margin: 0 auto;">
          {''.join(f'<li>{f}</li>' for f in focus_items)}
        </ul>
      </div>
    </section>

""" + cta_big(
        eyebrow="We can start this week",
        headline_html=f"Need <em>{title.lower()}</em> cover &mdash; this week?",
        lead="On-call, ad-hoc, or fully embedded. Tell us the shape and we'll come back same day with a fixed-scope proposal.",
        features=[
            "Same-day response on every business day",
            "Senior consultant on the work &mdash; no juniors",
            "Ad-hoc, project, or ongoing retainer &mdash; your call",
        ],
        stat_num_html="Same day",
        stat_label="every business day, no triage queue",
        badge_text="Senior consultant ready",
    )
    return dict(title=f"{title} Support", description=f"Specialist Jobpac {title.lower()} support for construction and civil businesses. Same-day response. Senior consultants only.", active="services", body=body)

PAGES["support-bookkeeping.html"] = support_subpage(
    "support-bookkeeping", "Bookkeeping", "BK",
    "Day&#8209;to&#8209;day Jobpac bookkeeping that <em>doesn't fall behind</em>.",
    "Bookkeeping inside Jobpac for construction and civil businesses &mdash; daily transaction processing, monthly close, BAS-ready books, and a clean GL handed to your accountant.",
    "We run your day-to-day Jobpac bookkeeping the way an in-house bookkeeper would &mdash; just without the cost or the resourcing risk. The work is done by senior bookkeepers who've spent years inside Jobpac, so your books reconcile, your GL is clean, and your accountant has nothing to chase at year-end.",
    [
        ("Daily transaction processing", "AP, AR, GL, bank feeds &mdash; processed daily so nothing piles up."),
        ("Bank &amp; credit card reconciliation", "All accounts reconciled to the GL, weekly or daily depending on volume."),
        ("Monthly close", "Period-end procedures, accruals, prepayments, and a closed-period sign-off."),
        ("BAS, IAS &amp; PAYG preparation", "Books readied to a standard your accountant can lodge from directly."),
        ("Year-end pack", "Trial balance, P&amp;L, balance sheet, schedules &mdash; handed to your accountant in a package they can use."),
    ],
    "What's not in scope.",
    [
        "We're bookkeepers, not your tax accountant. We don't lodge BAS or do tax returns &mdash; we hand the package to whoever does.",
        "Decisions about your accounting policy stay with you. We follow the policy and flag things that look off.",
        "We're not a triage queue &mdash; if a question is outside bookkeeping, we'll route it to the right Buoy specialist same day.",
    ],
)

PAGES["support-accounts-payable.html"] = support_subpage(
    "support-accounts-payable", "Accounts Payable", "AP",
    "Subbie claims, vendor invoices, and <em>clean</em> payment runs.",
    "Specialist Jobpac AP support: subbie claim processing, RCTI generation, vendor management, statutory compliance, and disciplined weekly payment runs &mdash; all inside the system you already pay for.",
    "Construction AP isn't normal AP. Retentions, RCTIs, statutory declarations, payment claim timeframes &mdash; the rules are different and the audit trail matters. Our AP team has spent careers processing claims for civil and commercial businesses, so the work goes through Jobpac the way it should &mdash; not around it.",
    [
        ("Outsourced invoice registration", "Supplier/SC Claims invoices captured and placed against the projects ready for coding, registered into Jobpac same day."),
        ("RCTI generation &amp; distribution", "Recipient-created tax invoices generated, distributed, and tracked &mdash; not stored in someone's email."),
        ("Statutory declarations", "Stat decs collected, attached to claim records, and held to the audit standard."),
        ("Vendor master maintenance", "ABN checks, banking, insurance currency, contractor licences &mdash; up-to-date and on file."),
        ("Weekly payment runs", "Run, approved, exported to your bank file format &mdash; on the same day, every week."),
        ("Subbie ledger reconciliation", "Your ledger reconciled to subbie statements monthly so disputes don't compound."),
    ],
    "How we plug into your team.",
    [
        "Drop-in: we cover when your AP person is sick, on leave, or behind.",
        "Embedded: a defined number of hours per week as your standing AP capacity.",
        "Project-based: cleaning up a backlog, then handing the running back to your team.",
    ],
)

PAGES["support-accounts-receivable.html"] = support_subpage(
    "support-accounts-receivable", "Accounts Receivable", "AR",
    "Progress claims out, retentions tracked, <em>money in</em>.",
    "Jobpac AR support for construction businesses: progress billing, customer invoicing, retention tracking, and disciplined collections of overdue accounts.",
    "Cashflow lives or dies on AR. Progress claims need to go out on the dot, retentions need to be tracked on both sides of the head contract, and overdue invoices need someone actually working them. Our team does the work in Jobpac so you have a single source of truth, not a spreadsheet running in parallel.",
    [
        ("Progress claim preparation", "Claims built against contract schedule of values, variations included, ready for issue on schedule."),
        ("Customer invoicing", "Standalone invoices, milestone bills, materials-on-site &mdash; raised against the right project line."),
        ("Retention tracking", "What's been withheld, when it's due to be released, and who needs reminding."),
        ("Aged debtors discipline", "Weekly aged debtor review, customer follow-ups documented, escalation path defined."),
        ("Disputes &amp; deductions", "Logged, tracked, and resolved &mdash; not allowed to age in a folder."),
    ],
    "Where AR usually breaks.",
    [
        "Progress claims go out late because the schedule of values is in someone's head, not the system.",
        "Retentions held by head contractors aren't tracked, so release dates pass unnoticed.",
        "Aged debtors get worse for three months until someone gets desperate and does a cleanup.",
        "Disputes sit in email instead of being formally logged in the customer record.",
    ],
)

PAGES["support-payroll.html"] = support_subpage(
    "support-payroll", "Payroll", "PR",
    "Construction payroll <em>done right</em> &ndash; Project Default Charges or based of Roles STP.",
    "Specialist Jobpac payroll support for construction and civil businesses: Project Job Costing, super, STP, leave, and timesheet integration.",
    "Construction payroll is a main area of Project Cost Control. Get the timesheet allocation wrong and your project costs are wrong too. We run construction payroll inside Jobpac with the rates, allowances, and on-costs configured the way you need it to be.",
    [
        ("Weekly &amp; fortnightly cycles", "Run end-to-end on schedule, with sign-off and bank file ready for upload."),
        ("Superannuation", "Contributions calculated, batched, and remitted on time."),
        ("Single Touch Payroll (STP)", "Each pay reported to the ATO under STP Phase 2 with the correct categorisations."),
        ("Leave administration", "Annual, personal, long-service, RDO accruals and balances reconciled monthly."),
        ("Timesheet integration", "Timesheets imported from your collection method, allocated to the right projects and cost codes."),
    ],
    "Why construction payroll trips most generalist providers.",
    [
        "EBAs vary by employer and by site &mdash; one rate sheet doesn't cover everyone.",
        "Allowances (site, travel, fares, meal) need to flow through to project cost, not just to the pay slip.",
        "Working time directives, RDOs, and rolling rosters complicate accruals.",
        "Subbie/labour-hire mixed workforces need clear separation in the GL and the project ledger.",
    ],
)

PAGES["support-profit-loss.html"] = support_subpage(
    "support-profit-loss", "Profit & Loss", "P&L",
    "A P&amp;L you can <em>trust</em>, on the same day every month.",
    "Monthly management packs, and forecast-vs-actual analysis built so leadership can act on the numbers.",
    "We will perform a Trial Balance reconciliation to ensure your financials are accurate.",
    [
        ("Entity P&amp;L", "Standalone and consolidated views for groups with multiple entities or joint ventures."),
        ("Monthly management pack", "Headlines, project schedule, exceptions, and commentary &mdash; ready for the leadership meeting."),
        ("Forecast-vs-actual", "Live variance reporting against the forecast, ranked so attention goes where it pays back."),
        ("Cashflow", "Linked cashflow forecast that updates as forecast and actuals shift."),
    ],
    "Why P&amp;L lateness compounds.",
    [
        "By the time the P&amp;L lands, the issues it shows are weeks old.",
        "Project managers can't course-correct on data they haven't seen yet.",
        "Forecast accuracy degrades because actuals never close back into the forecast cycle.",
        "Boards make decisions on stale numbers &mdash; or worse, on gut.",
    ],
)

PAGES["support-temp-relief.html"] = support_subpage(
    "support-temp-relief", "Temp Relief", "TR",
    "Short&#8209;term cover when you need it &mdash; <em>without the agency markup</em>.",
    "Specialist Jobpac temp relief: cover for sick leave, parental leave, holidays, or peak-period workload &mdash; senior bookkeepers and accountants who can land in your seat without three weeks of onboarding.",
    "When your finance person is suddenly out for two weeks &mdash; or six months &mdash; you don't have time to recruit, train, and ramp a temp. We slot a senior consultant who already knows Jobpac into the seat, with day-one productivity instead of week-three. The cost is roughly what an agency temp costs, and the output is a magnitude better.",
    [
        ("Sick leave / unplanned absence", "Same-week cover. We can be in by Monday morning if you call Friday afternoon."),
        ("Parental &amp; long-service leave", "Defined cover for a known period, with handover protocols both directions."),
        ("Holidays / annual leave", "Pre-booked cover for known absences &mdash; no scrambling."),
        ("Peak-period workload", "Year-end, EOFY, big project closeouts &mdash; extra hands without permanent overhead."),
        ("Hand-back kit", "Documented work-in-progress so your returning team-member isn't lost on day one."),
    ],
    "How we keep day-one productive.",
    [
        "We've already worked inside Jobpac for sixteen years &mdash; no orientation needed.",
        "We map your project structure and chart of accounts before we start, not while we're starting.",
        "Senior people only &mdash; no &quot;here's a graduate, good luck&quot;.",
        "We hand the seat back cleanly with a written handover, not a brain-dump email.",
    ],
)

PAGES["support-business-forecasting.html"] = support_subpage(
    "support-business-forecasting", "Business Forecasting", "FC",
    "Live business forecasts &mdash; built <em>inside</em> Jobpac, not next to it.",
    "Integrated revenue, project, and cashflow forecasting for construction and civil businesses &mdash; built and maintained in Jobpac so the forecast actually reflects the live business.",
    "Most construction businesses we meet have a forecast in Excel that someone built two years ago and patches each month. It's drifted from reality and nobody fully trusts it. We build the forecast inside Jobpac so it lives in the system that holds the truth &mdash; project costs, contract values, timesheets, and cashflow all feeding the same model.",
    [
        ("Project pipeline forecast", "Approved, probable, and possible jobs &mdash; with weighting and cashflow impact mapped to dates."),
        ("Project P&amp;L forecast", "Forecast cost-to-complete and forecast margin per project, updated as actuals close."),
        ("Entity-level revenue &amp; margin forecast", "Rolling 12 / 24 / 36-month view by entity and consolidated."),
        ("Cashflow forecast", "Linked to the project pipeline and AR/AP timing &mdash; not a static spreadsheet."),
        ("Forecast-vs-actual loop", "Each month-end, actuals close back into the forecast model so accuracy improves over time."),
    ],
    "Where most construction forecasts go wrong.",
    [
        "Built once in Excel, then never trued back to actuals &mdash; so accuracy drifts.",
        "Project pipeline lives in a CRM that doesn't talk to the cost system.",
        "Cashflow is a separate model that's been &quot;temporarily&quot; running for three years.",
        "Forecast vs actual variance is computed by hand, late, and not ranked.",
    ],
)


# ============================================================
# Run
# ============================================================
def ensure_inner_css():
    css_path = ROOT / "styles.css"
    css = css_path.read_text(encoding="utf-8")
    if INNER_CSS_MARKER in css:
        # Replace existing block — find from marker to EOF and replace
        idx = css.find(INNER_CSS_MARKER)
        css = css[:idx].rstrip() + "\n" + INNER_CSS.lstrip("\n")
    else:
        css = css.rstrip() + "\n\n" + INNER_CSS.lstrip("\n")
    css_path.write_text(css, encoding="utf-8")
    print(f"styles.css: {len(css):,} bytes")

def write_pages():
    for filename, page in PAGES.items():
        html = make_layout(page["title"], page["description"], page["active"], page["body"])
        (ROOT / filename).write_text(html, encoding="utf-8")
        print(f"  wrote {filename} ({len(html):,} bytes)")

def cleanup_orphans():
    """Remove pages that used to exist but no longer do (post-consolidation)."""
    orphans = ["team.html", "process.html", "support-invoice-registration.html"]
    for o in orphans:
        path = ROOT / o
        if path.exists():
            path.unlink()
            print(f"  removed orphan {o}")

if __name__ == "__main__":
    ensure_inner_css()
    write_pages()
    cleanup_orphans()
    print(f"\nDone. {len(PAGES)} pages.")
