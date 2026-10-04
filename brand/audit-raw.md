# Verdant Soft: raw audit capture

- **Captured:** 2026-10-04, local Claude Code session, Claude in Chrome (logged in to LinkedIn).
- **Scope:** raw facts only, no analysis. Follows the "Capture spec" in `brand/research.md`.
- **Text** was copied from the page text or DOM in Chrome, unless marked `(transcribed)` (typed from a screenshot).
- **Relative dates** ("2w", "8mo") are as LinkedIn displayed them on 2026-10-04.
- **Left out on purpose** (repo rules): employee counts, team-size figures, connection names, admin-only stats.
- **Status:** website and LinkedIn header/About are complete. The LinkedIn posts table is partial: captions marked `TBD` get filled in the next pass. Instagram, Clutch, Upwork and Fiverr are not captured yet.

---

## 1. Pages crawled

`/sitemap.xml` → 404 ("This page could not be found."). `/robots.txt` → 404. Pages below come from the header and footer nav, the Services dropdown and in-page links.

**Every page:** `<title>` = "Verdant Soft". Meta description = "Verdant Soft is a technology solutions company empowering businesses through innovative software, digital transformation, and scalable web and mobile applications." No `og:*` or `twitter:*` tags.

**Header nav (every page):** Logo → `/`. "Case Studies" → `/#case-studies`. "Services" (dropdown: Custom Software Development `/services/custom-software`, Cloud & DevOps `/services/cloud-devops`, IT Team Outsourcing `/services/it-team-outsourcing`, UI/UX Design `/services/ui-ux-design`). "FAQs" → `/#faqs`. "Careers" → `/career`. "Blogs" → `/#blogs`. Button "Get in Touch" → `/contact-us` (white text on #1b1b1b).

**Footer (every page):** Links: Case Studies, Services, FAQs, Careers, Blogs, Contact (`/contact-us`). Social icons: LinkedIn, Facebook, Instagram (see §8). Centre text: "Your brand deserves better." (grey #707070) / "Let's build it right." (white). Bottom row: white logo, "Privacy" `/privacy`, "Terms" `/terms`, "Email info@verdant-soft.com", "Phone +92 3268 282 488". There's a second (hidden, mobile) footer with the headings "Company" and "Legal" and links "Terms & Conditions" and "Privacy Policy".

**Shared FAQ block** (home, the service pages, and the blog pages as "Frequently Asked Questions"). Heading: "Smarter decisions start with clear answers." Answers read from the DOM after expanding each question:
- "How long does a typical project take?" — "The length of a typical project varies based on scope and complexity. Generally, projects can range from a few weeks to several months or more."
- "What if I don't know exactly what I need?" — "If you're unsure what you need, start by sharing your goals or interests, and we can help explore options with you. We can refine your ideas together to find the best solution."
- "Can I request just one service?" — "Absolutely! Please let me know which service you'd like to request, dev ops, web development, UI UX design or IT team outsourcing. I'll be happy to assist you."
- "How do payments work?" — "We follows a milestone-based payment schedule, ensuring transparency and mutual trust. Payments are structured at project initiation, key development phases, and final delivery."
- "What if I need changes after a project ends?" — "If you need changes after a project ends, contact us to discuss possible revisions or support options. Additional fees or a new agreement may apply."

### 1.1 Home: https://www.verdant-soft.com/
No `<h1>`; the hero headline is a `<p>`. In the text below, square brackets mark gradient-text words.
- **Hero:** "Empowering [Businesses Through] Technology" / "Innovative software solutions tailored to empower businesses and streamline operations. Committed to excellence in technology and customer satisfaction."
  - CTA "Book a Meeting" (button) → opens a modal with a Calendly iframe `calendly.com/verdant-soft-info/`.
  - CTA "Hire an Expert" → `/hire-us`. Both are outlined pill buttons with a black circular arrow icon.
- **Achievements:** eyebrow "Pioneering Trust and Innovation"; heading "[Verdant Soft] Achievements"; body "We take pride in empowering businesses worldwide with innovative solutions. Verdant Soft bring an unwavering commitment to excellence, backed by a global presence."
  - Animated counters, final values after the count-up finishes: "500+ Successful Projects" · "36+ Active Clients" · "95% Client satisfaction rate" · "5+ Years of expertise". Mid-animation they read lower (490+, 35+, 93%).
- **Services:** "[Not just services - we deliver] growth, clarity, [and] real impact." Four expandable cards, each linking to its service page:
  - "Custom Software Development": "We create innovatively customized software solutions precisely, tailored to your business needs, enhancing flexibility, scalability, and efficiency to drive sustainable growth."
  - "Cloud & DevOps": "We provide seamless DevOps and cloud solutions to optimize your application's performance, scalability, and reliability through tailored deployment, automation, and management."
  - "IT Team Outsourcing": "Our software house offers dedicated IT team outsourcing solutions, providing skilled professionals to empower your projects with high-quality technology services."
  - "UI/UX Design": "At our software house, we craft intuitive, visually stunning, innovative UI/UX designs that significantly enhance user engagement and deliver seamless, impactful digital experiences."
- **Case studies:** H2 "[Stories of our] transformations [across] Services [and] Industries". Eight tiles, each with "Explore More" → `/case-study/web/<slug>`: Psychiatric Clinic and Hospital Management System · E-commerce Platform · Real Estate Platform · Parking Application · VPN Extension & Subscription Management System · Dental Care & Learning Management System · Shopify Sync Platform · Clinic Management System.
- **Testimonials:** H2 "Real stories. Real winners. [Straight from our clients]". Carousel, see §6.
- **FAQ:** shared block, see above.
- **Blogs:** H2 "Stories, strategies, [and] creative perspectives [from the team.]". "All Blogs →" → `/all-blogs`. Three cards linking to `/blogs/cloud-optimization`, `/blogs/custom-software` and `/blogs/design-to-deployment`.

### 1.2 Custom Software Development: https://www.verdant-soft.com/services/custom-software
- H1 "Custom Software Development" (gradient). Bullets:
  - "We create tailored solutions specifically designed to meet your unique business needs."
  - "Our applications are built to grow with your business and adapt to changing requirements."
  - "We focus on streamlining workflows to improve productivity and operational performance."
  - "Our solutions empower your organization to innovate, expand, and stay competitive."
- "No guesswork, just a clear path from ideas → results." Six steps:
  1. Requirement Analysis: "Requirement analysis is the process of identifying, understanding, and documenting stakeholder needs to guide system development."
  2. Design & Planning: "Design & planning involve systematically creating and organizing ideas, strategies, and solutions to achieve specific goals effectively."
  3. Development: "The Development Phase involves coding, integrating, and building the software according to design specifications to create a functional product."
  4. Testing: "Custom software testing is tailored testing designed to verify that unique software features meet specific business requirements and quality standards."
  5. Deployment: "Launch the website to a live server, configure hosting, and ensure everything is functioning correctly in the production environment."
  6. Maintenance & Updates: "Monitor performance, fix bugs, update content, and add new features as needed for continuous improvement."
- "Custom Software Developement Technologies" (spelling as shown; possible typo):
  - Frontend: JavaScript, Kotlin
  - Backend: Node, Python, Php
  - Frameworks: React, Vue, Next, Django, Nest, Express, Konva
  - DataBase: MySql, MongoDb, Amazon Aurora, SQLite
- H2 "Projects [Highlights]". Ten links: Psychiatric Clinic, Canvas Platform (`/case-study/web/canvas`), Clinic Management System, E-Commerce Platform, ETL Management System (`/case-study/web/etl-management-system`), Dental Care & Learning Management System, Parking Application, Real Estate Platform, Shopify Sync Platform, VPN Extension & Subscription Management System.
- Images: `custom-software-service-bg.ec9d5145.png` (alt "custom-software-img4"); 32px technology logos.

### 1.3 Cloud & DevOps: https://www.verdant-soft.com/services/cloud-devops
- H1 "Cloud & DevOps". Intro: "Verdant Soft offers expert DevOps and cloud solutions to boost your application's performance, scalability, and reliability. We specialize in automation, CI/CD, and infrastructure as code to streamline deployment and reduce errors. Our tailored cloud management ensures secure, cost-effective, and scalable environments. Partner with us to accelerate innovation, minimize downtime, and stay ahead of the competition."
- Six steps:
  1. Plan & Develop: "Define project scope, user stories, and acceptance criteria. Create high-level architecture diagrams. Plan infrastructure, data flows, and integrations."
  2. Build & Test: "Automate builds using CI tools like Jenkins, GitLab CI, Travis CI. Run automated tests. Use testing frameworks and tools like Selenium, JUnit, TestNG."
  3. Integrate & Deploy: "Continuously integrate code changes and deploy them to staging or production environments through automated pipelines."
  4. Release: "Deploy to staging environment. Perform acceptance testing. Automate deployment for production release."
  5. Operate & Monitor: "Monitor applications in real-time, track performance, and manage infrastructure to ensure stability and availability."
  6. Feedback & Improve: "Gather feedback from monitoring and users, then iterate on development to improve performance, security, and features."
- "DevOps Tools & Integrations":
  - Clouds: AWS, Azure, GCP, Digital Ocean, Alibaba
  - CICD: GitHub, BitBucket, GitLab, Jenkins, CircleCI
  - Containerization & Orchestration: Docker, Kubernetes, OpenShift
  - IAC: Terraform, CloudFormation, Ansible
  - Monitoring & Logging: DataDog, "Prometheous" (as shown; possible typo), Grafana, ElasticSearch, Dynatrace
  - Operating System: Linux, Windows
  - Scripting & Automation: Bash, "Powsershell" (as shown; possible typo), Python, JavaScript, Go
- "Projects Highlights" (labels only): E-Commerce & Analytics Platform · QR Code Generating Platform · Staff Augmentation & IT services · E-Commerce Platform · BTech · Business Platform · Integration service of Microsoft365 · IT Services · Health Care System · Building Supplies & IT Innovator · IT Services · E-commerce Ecosystem · Tech Consulting.

### 1.4 IT Team Outsourcing: https://www.verdant-soft.com/services/it-team-outsourcing
- H1 "IT Team Outsourcing". Intro (third person, as shown): "Verdant Soft is a tech solutions provider focused on empowering businesses with innovative software development and IT services. They offer custom software, web and mobile apps, cloud services, and consulting. Their skilled team uses the latest technologies to deliver tailored, reliable solutions. Committed to quality and collaboration, Verdant Soft drives digital transformation and long-term growth for clients across various sectors."
- "Benefits of Partnering with Verdant Soft": Efficiency · Access to top-tier IT talent · Focus on strategic initiatives while we handle day-to-day IT operations · Scalability and flexibility · Risk mitigation with experienced professionals.
- "IT Team Outsourcing Services we offer":
  - Dedicated IT Teams: "Custom-built teams aligned with your business needs." / "Skilled professionals in software development, network management, support, and more." / "Flexible engagement models (full-time, part-time, project-based)."
  - Project-Based Outsourcing: "End-to-end management of specific IT projects." / "Agile and waterfall methodologies." / "Clear deliverables and timelines."
  - Managed IT Services: "Proactive monitoring and maintenance." / "24/7 support." / "Infrastructure management and cloud services."
  - Offshore Development: "Cost-effective development teams." / "Expertise across various technologies and industries." / "Seamless communication and collaboration."

### 1.5 UI UX Design: https://www.verdant-soft.com/services/ui-ux-design
- H1 "UI UX Design". Intro: "At our software house, we craft stunning, user-friendly UI/UX designs tailored to your brand and audience. Our collaborative process ensures seamless, responsive experiences across all devices. We focus on aesthetics, functionality, and user engagement to boost satisfaction and retention. Partner with us to elevate your digital presence and drive business success."
- Six steps:
  1. Research & Discovery: "Understand the users, business goals, and market context through interviews, surveys, and competitor analysis."
  2. User Personas: "Develop detailed user personas and map their journeys to understand needs, pain points, and key interactions for improved user experience."
  3. Architecture & Wireframing: "Organize content and structure through sitemaps and develop low-fidelity wireframes to outline layout and functionality."
  4. Design & Prototyping: "Design and prototyping in UI/UX involve creating visual layouts and interactive models to optimize user experience and functionality before development."
  5. Testing & Validation: "Conduct usability testing with real users, gather feedback, and identify areas for improvement."
  6. Implementation & Iteration: "Collaborate with developers for implementation, monitor performance post-launch, and iterate based on user feedback and analytics."
- "UI UX Design Tools & Technologies":
  - Design & Prototyping: Figma, Adobe XD, Sketch, InVision, Axure RP
  - Wireframing & Flowchart: Balsamiq, Whimsical, Lucidchart
  - Collaboration & Handoff: Miro, Zeplin
  - Additional Useful Tools: Photoshop, illustrator, "After Affects" (as shown; possible typo), Moqups

### 1.6 Hire an Expert: https://www.verdant-soft.com/hire-us
- Eyebrow "Team Outsourcing"; heading "Hire an Expert".
- Body: "Partner with us for seamless team outsourcing, ensuring expert support and flexible solutions.Enhance your business efficiency by leveraging our dedicated teams tailored to your needs." (No space after the first full stop, as shown.)
- "You can reach us by phone or mail, or you can just drop by the office."
- Location "772/A, G4 block, Johar Town, Lahore Pakistan." · Email info@verdant-soft.com · Phone +92 3268 282 488.
- Contact form with a "Submit" button. The form wasn't submitted.

### 1.7 Contact: https://www.verdant-soft.com/contact-us
- Eyebrow "Let’s Work Together"; heading "Connect Us!"
- Body: "Let’s create something amazing together! Reach out I’d love to hear about your project and ideas."
- Same contact block and "Submit" form as /hire-us.

### 1.8 Careers: https://www.verdant-soft.com/career
- H1 "Careers at Verdant Soft". "Join a team where passion meets purpose. Discover a career where your contributions are valued and where you can truly make a difference."
- "Why work with us?":
  - "We offer internal mobility opportunities"
  - "We provide an inclusive environment where everyone can thrive"
  - "You will discover a wide verity of industries and experiences" (as shown)
  - "Our strong collaborative teams place teamwork and sharing at the heart of their daily activities"
  - "We integrate CSR guidelines into our projects to have a positive impact on society and the environment"
- "Find the Role that Best Fits You!" → the job list shows "Something when wrong. Please check back later" (as shown on 2026-10-04).
- "Couldn't Find Your Position?" CTA "Send Your Resume".

### 1.9 Blogs: https://www.verdant-soft.com/all-blogs
Heading "All Blogs". Three posts. None shows a date or author.
- **/blogs/cloud-optimization**: H1 "Optimizing Cost and Performance in Cloud Architecture" (card title "Why Cloud Optimization Matters").
  - Sections: Why Cloud Optimization Matters · How Verdant Soft Helps You Balance Cost and Performance (Right-Sizing Your Resources, Smarter Scaling, Modern Architecture: Containers & Microservices, Multi-Cloud & Hybrid Strategies, Real-Time Monitoring & Proactive Alerts) · What Makes Verdant Soft Different? · Real Results Our Clients See · Thoughts.
  - Claims: "Reduced their monthly cloud costs by up to 40%" / "Increased system performance and uptime" / "Sped up release cycles through DevOps automation" / "Gained peace of mind with reliable infrastructure and support". "We don’t just "move" businesses to the cloud we work as your long-term technology partner."
  - CTAs: "👉 Explore our DevOps services". "Contact Verdant Soft for a quick, no-pressure consultation."
- **/blogs/custom-software**: H1 "Why You Should Invest in Custom Software Development".
  - Sections: Off-the-Shelf vs. Custom: What's the Difference? · Tailored to Your Needs · Smarter Scaling · Modern Architecture: Containers & Microservices (the body is about integrations) · Competitive Advantage · Increased Security & Control · What Verdant Soft Brings to the Table · Real-World Impact · Thoughts. A stray sub-heading "Why Cloud Optimization Matters" appears between sections (as shown).
  - Lines: "We don’t just write code we solve problems." / "At Verdant Soft, we believe software should work for you, not the other way around."
- **/blogs/design-to-deployment**: H1 "How Our Team Builds Digital Products: From Design to Deployment".
  - Phases 1–4: Understanding & UX/UI Design · Development & Engineering · Testing & Feedback Loops · Deployment & Launch.
  - Stack named: Figma, Adobe XD; React, Vue, HTML/CSS, Tailwind; Node.js, Laravel, Django; MySQL, PostgreSQL, MongoDB; AWS, Azure, Vercel.
  - "What Sets Verdant Soft Apart": "We're collaborative you're part of the process at every step" / "We're full-cycle strategy, design, development, deployment" / "We prioritize performance, usability, and scalability" / "Our solutions are tailored no one-size-fits-all shortcuts".
  - Closing: "At Verdant Soft, we bring together designers, developers, and DevOps engineers to deliver end-to-end solutions that not only work but work beautifully."

### 1.10 Case studies: /case-study/web/<slug>
Every case study uses the same layout: intro → "Technologies" → "Project Challenges" → "The Process" → "Solutions" → "Results and Impact".

"The Process" text is **identical on every case study**:
- Fast, Structured Onboarding
- Agile Execution for Rapid Progress (mentions "the migration")
- 24-Hour Workflow for Maximum Productivity: "The Polish team completed tasks and submitted approval requests during their workday, which the San Francisco team reviewed and responded to as their day began."
- Independent Work Model for Faster Delivery

| Slug | Title | Technologies | Intro (first sentence, verbatim) |
|---|---|---|---|
| psychiatric-clinic | Psychiatric Clinic and Hospital Management System | Next Js, Node Js, Express Js, Postgre SQL | "We developed a comprehensive healthcare management system for a psychiatrist and therapist clinic, aimed at streamlining mental health service delivery." … "Our team specifically contributed by building the medications, allergies, visits, and lab orders modules." |
| e-commerce | E-Commerce Platform | Next Js, Node Js, Nest Js, Postgre SQL | "We developed a robust, role-based e-commerce CMS platform designed to empower businesses in efficiently managing the backend operations of their online stores." |
| real-estate | Real Estate Platform | React, Python, Django, MongoDB | "We developed an innovative real estate platform designed to simplify and modernize the entire property transaction experience." (The Solutions list repeats one line twice, as shown.) |
| parking-app | Parking Application | React Js, Node Js, Express Js, Postgre SQL | "We developed a zone-based parking application that offers users a convenient, secure, and intuitive way to manage their parking sessions." (Solutions mention NestJS and Stripe.) |
| vpn-extension | VPN Extension & Subscription Management System | React Js, TypeScript | "We developed a secure and user-friendly VPN browser extension designed to enhance internet privacy and protection." |
| dental-care | Dental Care & Learning Management System | Next Js, Typescript, Postgre SQL | "We built a comprehensive digital platform specifically designed for the dental industry, bringing together patient services, professional education, and digital consent management into a single, unified ecosystem." |
| shopify | Shopify Sync Platform | Vue Js | "We developed a seamless integration between a Shopify store and a Vue.js application, enabling real-time synchronization of products, collections, and orders." |
| clinic-management | Clinic Management System | React Js, Node Js, Nest Js, Postgre SQL | "We developed a comprehensive clinical management platform aimed at streamlining clinic operations and enhancing the patient booking experience." |
| canvas | Canvas Platform | Vue.js, Konva.js | "We developed a dynamic, browser-based design canvas inspired by tools like Figma, using Konva.js and Vue.js." |
| etl-management-system | ETL Management System | Python | "We contributed to the development of a scalable integration platform with a multi-tenant architecture, purpose-built to streamline data synchronization and ETL workflows across a variety of client environments." |

No client names appear on the case-study pages.

### 1.11 Legal
- **/terms**: H1 "Terms & Conditions". H2s include Acceptance of Terms, Services, Use of Website, Intellectual Property, Payment and Billing. Body not captured.
- **/privacy**: H1 "Privacy Policy". H2s include Information We Collect, How We Use Your Information, Sharing Your Information, Cookies and Tracking Technologies, Data Security. Body not captured.

---

## 2. Palette

**Method.** Computed styles of every visible element on the homepage, read in Chrome: `color` on text, `background-color`, `border-color`, SVG `fill`/`stroke`, and background gradients. Area share = summed element area of that background ÷ page area (5042px tall, desktop). Elements overlap, so the shares are rough. Custom properties are from the site's main CSS file (`/_next/static/css/ffbd0fe497045ec9.css`).

| Hex | CSS source | Where used (homepage) | Rough area |
|---|---|---|---|
| #ffffff | `--color-white`; body background `oklch(1 0 0)` | Page background; text on dark buttons and footer; 4 SVG fills | 17% (as bg) |
| #f9f9f9 | `--color-gray` (also `bg-[#F9F9F9]`) | Nav bar, hero panel, service cards, blog cards, FAQ rows | 28.5% |
| #f9f9f9 at 85% alpha | `bg-[#F9F9F9D9]` | 7 panels/cards | 10% |
| #1b1b1b | `--color-footer-black` | Footer background; "Get in Touch" button bg; dark heading text (h2 and hero text) | 15.5% |
| #5e5e5e | `--color-black` (the variable named "black" is #5e5e5e) | Body text, h4 testimonial names, nav links, card text | text only |
| #5e5e5e at 80% alpha | `text-black/80` | Small text in 7 spans | text only |
| #707070 | `text-[#707070]` | Secondary text, "All Blogs", footer "Your brand deserves better." | text only |
| #416d95 → #74afad | `--color-green-gradient: linear-gradient(102.32deg,#416d95,#74afad)`. Computed in Chrome as `linear-gradient(102.32deg, rgb(65, 109, 149), rgb(116, 175, 173))` | Gradient text (background-clip) on highlighted heading words; 15 elements | text only |
| #406c94 | `bg-[#406C94]` | 1 div (homepage); purpose not identified | 1.3% |
| #26615e | `bg-[#26615E]` | 1 div (homepage); purpose not identified | 1.3% |
| #000000 | `--color-pure-black` | 18 SVG path fills (arrow icons), 2 spans | — |
| #fdc700 | (SVG) | Star-rating icons in testimonials (fill and stroke) | — |
| #d1d5dc | (SVG) | 14 SVG paths (fill and stroke); element not identified | — |
| #ffffff at 10% alpha | `border-white/10` | 9 borders in the footer area | — |

**Other custom properties defined in the CSS** (not seen in the homepage computed scan):
- `--color-revert-green-gradient: linear-gradient(90deg,#fff,#74afad)`
- `--color-soft-green-fade: linear-gradient(90deg,#fff,#416d95 34.13%,#74afad 63.94%,#fff)`
- shadcn-style tokens in `oklch`: `--background: oklch(100% 0 0)`, `--foreground: oklch(14.5% 0 0)`, `--primary: oklch(20.5% 0 0)`, `--secondary/--muted/--accent: oklch(97% 0 0)`, `--muted-foreground: oklch(55.6% 0 0)`, `--border/--input: oklch(92.2% 0 0)`, `--ring: oklch(70.8% 0 0)`, `--destructive: oklch(57.7% .245 27.325)`, `--chart-1…5`, `--radius: .625rem`, plus a `.dark` set.
- Library variables: `--swiper-theme-color: #007aff`; react-toastify `--toastify-*`.
- Tailwind palette: `--color-gray-100…800`, `--color-red-500`, `--color-yellow-400`.

**Logo colours** (pixels sampled in Chrome from the logo files):
- Header logo (`verdant-green-logo…svg`): opaque pixels cluster around #406090 and #307080 (quantised); bluest about #416c96.
- `apple-touch-icon.png`: gradient from about #416c96 / #436e96 (blue, top) to about #86bbb7 (light teal, bottom), on a white square.
- `favicon.png`: range #245785 (darkest) to #91d2cd (lightest).
- The white footer logo is pure #ffffff.

## 3. Fonts

- **Family:** Inter, everywhere. Computed `body` font-family: `Inter, "Inter Fallback"`. Source: self-hosted woff2 files under `/_next/static/media/` via `@font-face` (Next.js font loading). The fallback is `local("Arial")` with metric overrides. No Google Fonts `<link>`.

| Element | Computed (homepage unless noted) |
|---|---|
| Hero headline (a `<p>`) | Inter 700, 48px, #1b1b1b; highlighted words in gradient |
| h1 (service pages) | Inter 700, 48px, #1b1b1b + gradient words |
| h2 (section headings) | Inter 600, 48px/48px and 36px/40px, #1b1b1b + gradient words |
| Other section headings (`<p>`) | Inter 600, 36px; service card titles 600, 24px |
| h4 (testimonial names) | Inter 600, 18px/28px, #5e5e5e |
| Body text | Inter 500, 16px/20px and 20px/25px, #5e5e5e; 600, 16px white on dark |
| Buttons and links | Inter 400, 14px/20px (white on dark); 400, 16px #5e5e5e; 500, 14px |
| Nav links | Inter 400, 18px/28px, #5e5e5e ("Get in Touch" white) |

Letter-spacing is `normal` throughout.

## 4. Logo

All files are downloaded into `brand/assets/` with their original names. Sizes match what the server reported in Chrome.

| File | URL | Format | Where used | Variant |
|---|---|---|---|---|
| verdant-green-logo.8bcaebdb.svg | https://www.verdant-soft.com/_next/static/media/verdant-green-logo.8bcaebdb.svg | SVG wrapping one embedded PNG (852×204); no vector paths; 72 KB | Header (alt "logo-white"), 128×31 rendered | Full lockup (VS mark + "Verdant Soft"), blue→teal gradient, for light backgrounds |
| verdant-white-logo.e0d6cd95.svg | …/_next/static/media/verdant-white-logo.e0d6cd95.svg | SVG wrapping one embedded PNG (4096×981); 265 KB | Footer bottom row (alt "logo-white"), 160×38 | Full lockup, all white, for dark backgrounds |
| VS.05a1a937.svg | …/_next/static/media/VS.05a1a937.svg | True vector SVG, 1 path, `fill="white"`, 1518×1342 viewBox; 4.6 KB | Footer `<img>` (alt "logo-white"), hidden at desktop width | Mark only (VS), white |
| VS-Green.770a6db3.svg | …/_next/static/media/VS-Green.770a6db3.svg | SVG wrapping one embedded PNG (2160×2160); 146 KB | Footer background `<img>`s (alt "Verdant background left/right/bottom"), hidden at desktop width | Mark only, gradient |
| VerdantLogoLeft.ee8822eb.png | …/_next/static/media/VerdantLogoLeft.ee8822eb.png | PNG 2160×2160 RGBA; 109 KB | Footer background, left (alt "Verdant background left"), shown large and faint | Mark only, gradient, offset in a transparent square |
| VerdantLogoRight.ee8822eb.png | …/_next/static/media/VerdantLogoRight.ee8822eb.png | PNG 2160×2160; **byte-identical to the Left file** (same SHA-1) | Footer background, right | Same as above |
| favicon.png | https://www.verdant-soft.com/favicon.png | PNG 66×58 | `<link rel="icon" type="image/x-icon">` | Mark only, gradient |
| favicon.ico | https://www.verdant-soft.com/favicon.ico | ICO (16×16, 32×32) | Not linked in `<head>`; served at the default path | Mark only |
| apple-touch-icon.png | https://www.verdant-soft.com/apple-touch-icon.png | PNG 180×180 | Not linked in `<head>`; served at the default path | Mark only, gradient, on white |

- No `og:image`.
- LinkedIn uses the gradient mark on white as its avatar. The LinkedIn banner shows the gradient lockup with "ENGINEERING TOMORROW’S TECH TODAY!" `(transcribed)`.

## 5. Imagery

- **Home**
  - Hero: a large light-grey (#f9f9f9) rounded panel with faint grey-blue line-and-node mesh illustrations, lower left and right (`dottedBg.5b4490b3.svg`). No photo.
  - Achievements and services: no imagery, only text cards on #f9f9f9.
  - Case-study tiles: small rounded tiles with darkened, mostly greyscale images and white titles. Contents: an e-commerce dashboard UI on black; two phone mockups (parking app); a hand over a laptop (real estate); clinic and doctor photos; a dental-procedure photo; a hacker-style laptop (VPN); a Shopify/Salesforce icon graphic.
  - Testimonials: white cards with yellow stars, plus 2 video cards. Poster of the Nedjmati video: a man in a suit and tie on a teal-blue background, large white text "ILYES ABDERREZAK" and a pill "PRODUCT OWNER" `(transcribed)`.
  - Blog cards: stock photos.
    - Greyscale hand with a cloud and network dots on a bokeh background.
    - Full-colour hand over a laptop holding a glowing cloud with circular icons (teal-blue cast).
    - Greyscale open office with developers at monitors.
  - Footer: #1b1b1b with very large, faint VS mark shapes cropped at left and right.
- **Service pages:** a hero image (`custom-software-service-bg.ec9d5145.png` on custom-software; not visually reviewed); step diagrams built from SVG lines and ellipses; 32px technology logo icons; and on custom-software, project cards with 376×200 screenshots (`*-image-1/2.png`). The other service pages' images were not visually reviewed.
- **Case studies, blogs, careers, contact:** not visually reviewed (text captured only).

Reference screenshots: `brand/audit/screens/site-home-01.jpg` … `site-home-08.jpg` (top to bottom of the homepage, desktop width).

## 6. Testimonials, verbatim

Source: https://www.verdant-soft.com/ (testimonial carousel, Swiper). There are 9 slides: 7 text and 2 video.
- Each text slide holds a **short version** (visible) and a **full version** (in the DOM, shown on expand or hover). Both are copied below exactly, including punctuation.
- No company is shown for anyone except Nick Kuijpers and Shervin Khanzadi.
- Ratings are as displayed.

1. **Elia Essen** · no title or company shown · 4.7/5
   - Short: "Working with Verdant Soft has been an absolute pleasure. Their expertise in the MERN stack, especially React. js, is truly impressive."
   - Full: "Working with Verdant Soft has been an absolute pleasure. Their expertise in the MERN stack, especially React. js, is truly impressive. They took full ownership of our AI SaaS platform, delivering high-quality, scalable, and visually stunning features that exceeded our expectations."
2. **Video**: `/videos/alex-video-3.mp4` · 4.5/5 · no name text on the slide · not transcribed.
3. **Video**: `/videos/nedjimeti.mp4`, poster `/nedjimeti-image.png` · 5/5. Poster text `(transcribed)`: "ILYES ABDERREZAK" / "PRODUCT OWNER". Not transcribed.
4. **Nick Kuijpers** · "CEO Wemasy" · 4.6/5
   - Short: "Verdant Soft has proven to be a highly supportive and reliable partner in the development of our company."
   - Full: "Verdant Soft has proven to be a highly supportive and reliable partner in the development of our company. Their team takes a thoughtful approach to analyzing issues and delivering effective solutions."
5. **Hesham Elkouha** (the DOM text has a leading space: " Hesham Elkouha") · no title · 4.5/5
   - Short: "It was a pleasure working with Verdant Soft very professional and delivered the work as expected."
   - Full: "It was a pleasure working with Verdant Soft very professional and delivered the work as expected. Their response time was also amazing."
6. **Waqas Zahoor Pal** · no title · 4.3/5
   - Short: "The job was completed perfectly with full cooperation and professional conduct."
   - Full: "The job was completed perfectly with full cooperation and professional conduct. I never expected an emergency task to be handled this efficiently, but Verdant Soft demonstrated that with hard work and dedication, anything is possible."
7. **Shervin Khanzadi** · "CEO Alogirft" · 4.8/5
   - Short: "Verdant Soft is a team of highly professional front-end developers with a strong and diverse skill set."
   - Full: "Verdant Soft is a team of highly professional front-end developers with a strong and diverse skill set. Their commitment to delivering high-quality results was evident throughout our collaboration."
8. **Isana Sebastian** · no title · 5/5
   - Short: "Working with Verdant Soft was a great experience. They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution."
   - Full: "Working with Verdant Soft was a great experience. They quickly understood our problem, collaborated effectively with our team, and delivered a solid solution. Their proactive communication, thoughtful suggestions, and flexibility made the process smooth."
9. **Ben Kemboi** · no title · 4.5/5
   - Short: "Verdant Soft completed the work in a timely manner. The team sought a clear understanding before starting the work."
   - Full: "Verdant Soft completed the work in a timely manner. The team sought a clear understanding before starting the work. They maintained positive communication and were ready to edit the work when asked to do so."

The Clutch review (research P01) is not on the website.

## 7. Fact checks

| Item | As displayed | Where |
|---|---|---|
| Tagline "Engineering tomorrow's tech today!" | **Not found on verdant-soft.com** (all pages in §1). On LinkedIn the tagline under the page name reads "Engineering Tomorrow’s Tech Today!" (curly apostrophe, title case), and the banner image reads "ENGINEERING TOMORROW’S TECH TODAY!" `(transcribed)`. | https://www.linkedin.com/company/verdant-soft/ |
| Founding year (2019?) | **Not shown on the website.** The closest item is the homepage counter "5+ Years of expertise". LinkedIn About shows no "Founded" field. | https://www.verdant-soft.com/ ; https://www.linkedin.com/company/verdant-soft/about/ |
| "Alogirft" | Shown exactly as "CEO Alogirft" under Shervin Khanzadi. Possible typo. | https://www.verdant-soft.com/ (testimonials) |

Other on-site spellings, recorded as shown (possible typos):
- "Custom Software Developement Technologies"
- "Prometheous"
- "Powsershell"
- "After Affects"
- "a wide verity of industries"
- "Something when wrong. Please check back later"
- "We follows a milestone-based payment schedule"
- "Verdant Soft bring an unwavering commitment"
- "React. js"
- "Useability Testing" (on LinkedIn post image P17, transcribed)

## 8. Social links

From the site footer. The header has no social links.
- LinkedIn: https://www.linkedin.com/company/101573750 (resolves to https://www.linkedin.com/company/verdant-soft/)
- Facebook: https://www.facebook.com/people/Verdant-Soft/61572806245482/
- Instagram: https://www.instagram.com/verdant_soft/
- Also: "Book a Meeting" opens Calendly `https://calendly.com/verdant-soft-info/`. Email info@verdant-soft.com.

## 9. LinkedIn company page

Viewed as a member ("View as member"), so admin-only data is not recorded.

- **URL:** https://www.linkedin.com/company/verdant-soft/ (numeric ID 101573750)
- **Name / tagline:** "Verdant Soft" / "Engineering Tomorrow’s Tech Today!"
- **Header line:** "IT Services and IT Consulting · Lahore · 10K followers". Post headers show "9,967 followers".
- **About / Overview (verbatim):** "At Verdant Soft, we are committed to driving innovation and excellence in the world of IT. As a dynamic and forward-thinking software company, we specialize in providing top-tier IT solutions and services designed to meet the evolving needs of businesses across various sectors."
- **Website:** www.verdant-soft.com
- **Industry:** IT Services and IT Consulting
- **Specialties:** not shown
- **Founded:** not shown
- **Location:** "772A, G4 Block, Johar Town, Lahore, PK"
- **Banner** `(transcribed)`: white left area with a dot grid, gradient VS lockup "Verdant Soft", subline "ENGINEERING TOMORROW’S TECH TODAY!" in dark navy italic caps, teal/blue wave shapes and outlined rounded squares on the right.
- **Avatar:** gradient VS mark on white.
- **Ads:** the sidebar shows "See a collection of active or past ads by Verdant Soft. View ad library".
- **Screenshot:** `brand/audit/screens/linkedin-header.jpg` (cropped to the page card).

### 9.1 Posts (feed "All", newest first as LinkedIn ordered them; captured 2026-10-04)

- Reactions, comments and reposts are the counts shown, with reactor names left out.
- "Edited" is as shown.
- Screenshots in `brand/audit/screens/li-post-NN.jpg` are cropped to the post column and show the media (first page only for documents).
- `TBD` = caption still to be filled from page text.

| # | Age | Format | Topic | Visual (what the image shows) | First caption line | Length | Hashtags / emoji | React · Comm · Repost | Screenshot |
|---|---|---|---|---|---|---|---|---|---|
| 00 | 1w | Document, "Tech Myths · 7 pages" | Tech myths vs facts | Dark navy-blue tech background with circuit lines; small white VS lockup top-left; huge "TECH ? MYTHS" ("TECH" dark, "MYTHS" white); "Things about technology you might still believe"; white humanoid robot holding a laptop, glowing blue icons. 3D/AI-style render. | "💻 Let's clear up a few tech myths. 👀" `(transcribed)` | medium | #VerdantSoft #DigitalMyths #TechFacts #SoftwareTrends #ITSolution `(transcribed)` | 11 · 0 · 1 | li-post-00.jpg |
| 01 | 2w, Edited | Document, "Is your business ready for its next growth phase? · 6 pages" | Growth / scaling | White-grey background with faint network lines; gradient VS lockup; "Is Your Business Ready for its Next Growth Phase?" ("Growth Phase?" in blue-teal); "Bigger goals. Higher expectations. More to manage / Growth brings opportunities and more complexity"; cut-out photo of a woman in a dark suit climbing floating dark steps, one step teal. | "Growth shouldn’t be held back by technology. 🚀" `(transcribed)` | medium | #VerdantSoft #BusinessGrowth #DigitalTransformation #Technology #SoftwareSolutions #BusinessScaling; link www.verdant-soft.com `(transcribed)` | 1 · 0 · 0 | li-post-01.jpg |
| 02 | 1mo | Image ×3 (collage) | New hires (3 interns/trainees) | "WELCOME ON BOARD" template: white, navy-blue headline, "New Perspective, New Energy / Stronger Together", blue-grey circles, dot grids, cut-out employee photo in a circle, name + role, "Let's build Something amazing!" pill + www.verdant-soft.com. One card per hire. | "🎉 We’re excited to introduce the newest members of the Verdant Soft team, bringing fresh ideas, energy, and enthusiasm to our journey of growth and innovation." `(transcribed)` | long | #VerdantSoft #WelcomeOnBoard #TeamVerdantSoft #BusinessDevelopment #UIUX #Internship #NewBeginnings #GrowingTogether `(transcribed)` | 29 · 1 · 1 | li-post-02.jpg |
| 03 | 3w | Image (portrait) | New hire (Junior Software Engineer) | Same template family: "WELCOME to the Team!" (navy + black), "New Perspective, New Energy / Stronger Together", "We’re thrilled to welcome [name] to Verdant Soft as our new Junior Software Engineer!", cut-out photo in a circle. | "🎉 We’re excited to introduce a new member of the Verdant Soft team, bringing unique skills, energy, and vision to our journey of innovation." `(transcribed)` | long | #VerdantSoft #JuniorSoftwareEngineer #SoftwareDeveloper #TechJobs #ITJobs #NewJoiner #StartYourCareer `(transcribed)` | 40 · 4 · 1 | li-post-03.jpg |
| 04 | 2mo | Text + lnkd.in link | Job: Business Development Intern | No image | "🚀 Exciting opportunity!" `(transcribed)` | medium | 🚀 | 21 · 5 · 2 | li-post-04.jpg |
| 05 | 2mo, Edited | Image ×3 (collage) | Office "Mango Day" celebration | Yellow/white template, script title "mango day" in yellow, gradient VS lockup, framed photos of the office decorated with yellow and white balloons and "MANGO DAY" letters, group photos; "Ripe with flavor, rich in goodness, Mango makes every day a little brighter!" `(transcribed)` | "We had an amazing time celebrating Mango Day at Verdant Soft" + emoji `(transcribed)` | long | TBD | 40 · 1 · 0 | li-post-05.jpg |
| 06 | 1mo, Edited | Video | Client video testimonial (Nedjmati) | Talking-head video: a man in an office chair, plants behind, VS watermark top-right, burned-in subtitles | "🧠What our clients say matters to us." `(transcribed)` | medium | TBD | 9 · 0 · 3 | li-post-06.jpg |
| 07 | 3mo | Document, "Where Talent, Teamwork & Creativity Meet · 5 pages" | Team culture / collaboration | Muted teal-grey photo background (faded); white brush-stroke banner "Team Collaboration" in blue; "in Challenging Projects"; "How Verdant Soft teams work together to solve complex challenges, deliver quality solutions, and achieve project success." `(transcribed)` | "At Verdant Soft, every workday is powered by collaboration, creativity, and the unique energy of our team." `(transcribed)` | long | TBD | 19 · 0 · 2 | li-post-07.jpg |
| 08 | 2mo | Link card "Apply \| Cheesyhire" (cheesyhire.com) | Job application link | Link preview card only | TBD | TBD | TBD | 8 · 2 · 0 | li-post-08.jpg (shows the link card + next post) |
| 09 | 8mo | Document, "VS Career Fair 2026 · 2 pages" | Campus career fair (FCCU, Riphah) | Lined notebook-paper background, gradient VS lockup, "#Careerfair2026", "11th Feb 2026", phone mockup with calendar and cards ("FCCU Career Fair 2026", "Riphah University FYP Evaluation", "Job Openings: 1. Business Development Executive 2. DevOps Engineer 3. UI/UX Designer"), polaroid "Note: Forman Christian College & University Career Fair 2026", sticky notes, "#Catchus", "#Verdantsoft" `(transcribed)` | "Save the date, your campus just made the high list 😉" `(transcribed)` | medium | #verdantsoft #careerfair #techcareers #FCCU #RIU `(transcribed)` | 21 · 0 · 1 | li-post-09.jpg |
| 10 | 5mo | Video | TBD | Video frame did not load | TBD | short | TBD | 17 · 0 · 1 | none |
| 11 | 8mo | Image ×4 (collage) | "Why choose Verdant Soft" stats | Dark navy/indigo with glowing purple-blue wave lines, white VS lockup, "WHY CHOOSE VERDANT SOFT?" ("WHY CHOOSE" light blue), stat boxes "50+ Scalable & Secure Solutions", "1M+ Global Users Reached", "69+ Websites Launched" `(transcribed, small text)`; side images "EXPERT TEAM …" (team-size figure omitted per rules), "ON-TIME DELIVERY", "AFFORDABLE PRICING & PLANS", www.verdant-soft.com | "Delivering quality, on time - powered by expert teams and proven results." `(transcribed)` | short | TBD | 21 · 0 · 2 | li-post-11.jpg |
| 12 | 8mo | Image ×2 | Event: Women Entrepreneurial Punjab Expo (WEPX 2026) | Navy-blue cards: "WOMEN ENTREPRENEURIAL PUNJAB EXPO / Team Verdant Soft at WEPX 2026" over a photo of four team members at a pink WEPX booth; second card "Supporting Women Entrepreneurs and Building a Future Driven by Innovation" with three event photos `(transcribed)` | "Verdant Soft at Women Entrepreneurial Punjab Expo (2026)" `(transcribed)` | long | TBD | 36 · 0 · 0 | li-post-12.jpg |
| 13 | 10mo | Image | Hiring | Navy gradient; white VS lockup; huge stacked "HIRING / HIRING / HIRING" (white, yellow, white); www.verdant-soft.com | TBD | long | TBD | 12 · 0 · 1 | li-post-13.jpg |
| 14 | 10mo | Image | UI quiz / engagement | Navy gradient; "WHICH UI IS MORE ACCURATE?"; two contact-card UI variants labelled "SQUAD A" / "SQUAD B"; blue thumbs-up and yellow lightbulb circle icons; www.verdant-soft.com | TBD | long | TBD | 6 · 2 · 0 | li-post-14.jpg |
| 15 | 10mo, Edited | Image | Hiring: Human Resource Generalist | Navy background, outlined "HIRING" stacked text behind a photo of a smiling young woman with glasses in a maroon sweater typing on a laptop (stock or AI-style photo); yellow "HUMAN RESOURCE GENERALIST" | TBD | long | TBD | 21 · 0 · 2 | li-post-15.jpg |
| 16 | 11mo | Image | DevOps toolchain | Navy gradient; "THE ULTIMATE DEVOPS TOOLCHAIN" (white/blue italic caps); "From code to deploy, DevOps runs on automation."; table: Infrastructure: Terraform, Ansible / Containers: Docker, Kubernetes / CI/CD: Jenkins, GitHub Actions / Monitoring: Prometheus, Grafana; "The right tools don't just build. They accelerate innovation." `(transcribed)` | TBD | medium | TBD | 7 · 0 · 0 | li-post-16.jpg |
| 17 | 11mo | Image | UI vs UX | Dark charcoal-to-maroon gradient; thin white line drawing "UI \| UX" with a pen nib; blue lists "Useability Testing, User Research, User Stories, Personas" and "Layout, Visual Design, Branding, Color Scheme, Typography" `(transcribed)`; www.verdant-soft.com | TBD | medium | TBD | 4 · 0 · 0 | li-post-17.jpg |
| 18 | 11mo, Edited | Image | Case study: Psychiatric Clinic and Hospital Management System | Navy gradient; "PSYCHIATRIC CLINIC AND HOSPITAL MANAGEMENT SYSTEM" (white condensed caps); monitor mockup with the app UI; tech badges "Node Js", "TypeScript", "Next.js"; www.verdant-soft.com | TBD | long | TBD | 8 · 1 · 2 | li-post-18.jpg |
| x1 | TBD | Image | Services overview | White background; gradient VS lockup; "We build more than software." / "Digital experiences that matter" (navy); teal chips "Is your website slow?", "Does your business need automation?", "Do you need a custom app?", "Here's how Verdant Soft can help."; laptop on a white 3D platform with floating teal icons; service grid: Web Development, UI / UX Design, DevOps Development, Web Services, Marketing, Business Development `(transcribed)` | TBD | TBD | TBD | TBD | li-post-x1.jpg |
| x2 | 9mo, Edited | TBD | Team trip | Not seen | "Kashmir Trip Highlights 2025:" `(transcribed)` | TBD | TBD | TBD | none |

Engagement summary: TBD (after captions are filled).

## 10. Instagram
Not captured yet. The site footer links to https://www.instagram.com/verdant_soft/.

## 11. Clutch, Upwork, Fiverr
Not captured yet.
