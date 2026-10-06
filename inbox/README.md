# News inbox (optional)

**What it's for:** real things the internet won't show yet, such as:
- an upcoming event, a new hire, a campus drive, a culture day (Mango Day), an expo
- a new client review, a launch, a milestone
- photos from any of the above

**Optional:** research runs automatically, so nothing breaks when this folder is empty. When it's empty, Grow with us stays conceptual.

**How an item is used** (`STYLE_GUIDE.md` §3 `CONTENT-MIX-v1` → `overrides`):
- An inbox item **takes the day.** It replaces that day's external post, never a Verdant slot.
- **Max one per day;** the rest queue, oldest first.
- If the month's Verdant share would go above 40%, the item waits for the next month.
- **Real photos** are allowed only from here, and only with the consent of everyone identifiable in them.
- **Hiring posts** use only roles supplied here. The pipeline never invents roles.

## How to add an item
Make a folder `inbox/YYYY-MM-DD-short-name/` with an `item.md` inside, plus any photos (JPG or PNG; don't upload originals over 5 MB). Copy this template into `item.md`:

```yaml
what: "One or two sentences: what happened or will happen."
when: "YYYY-MM-DD (the event date)"
post_on_or_after: "YYYY-MM-DD"
post_before: "YYYY-MM-DD or null"
people_named: []          # names exactly as they should appear; leave empty if none
consent: false            # true only if everyone identifiable in the photos agreed to be posted
photos: []                # file names in this folder
links: []                 # public links, if any (job post, event page)
contact: "who to ask if something is unclear"
facts_ok_to_state: []     # exact facts we may say (dates, role titles, place)
do_not_say: []            # anything that must stay private
```

## Rules for the pipeline
- **Words:** state only what's in `what`, `facts_ok_to_state` and the linked public pages, never anything from `do_not_say`.
- **Consent:** no photo is posted unless `consent: true`.
- **Afterwards:** once posted, add `posted: posts/<file>.md` to the item. Don't delete the folder; it's the record.
- **Privacy:** this repository is public. Put nothing here that isn't meant to be public. Private items go through a private channel, to be decided before launch.
