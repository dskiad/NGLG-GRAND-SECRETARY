# NGLG Letter Manager — Ψηφιακή Μεγάλη Γραμματεία

Εσωτερική web εφαρμογή της **Εθνικής Μεγάλης Στοάς της Ελλάδος** για γρήγορη δημιουργία, πρωτοκόλληση, αρχειοθέτηση και επαναχρησιμοποίηση επίσημων επιστολών.

Η εφαρμογή έχει σχεδιαστεί για χρήση από τη **Μεγάλη Γραμματεία** και από εξουσιοδοτημένους συνεργάτες, με πρόσβαση μέσω email και OTP.

## Βασικές λειτουργίες

- Αυτόματος αριθμός πρωτοκόλλου ανά έτος.
- Αυτόματη ημερομηνία εγγράφου.
- Σταθερό επίσημο επιστολόχαρτο.
- Επίσημο έμβλημα, υπογραφή και σφραγίδα.
- Πεδία παραλήπτη, email, θέματος και κειμένου.
- Πρότυπα ανά περίπτωση, όπως:
  - Επίσκεψη Μεγάλου Διδασκάλου
  - Επίσκεψη Μεγάλου Διδασκάλου με εκπρόσωπο
  - Συλλυπητήρια
  - Συγχαρητήρια
  - Ευχαριστήρια
  - Πρόσκληση
  - Ανακοίνωση
- Αρχείο επιστολών με αναζήτηση κατά:
  - αριθμό πρωτοκόλλου,
  - θέμα,
  - ημερομηνία,
  - παραλήπτη,
  - email παραλήπτη.
- Δυνατότητα **«Νέα πάνω σε αυτή»** ώστε μια παλαιά επιστολή να χρησιμοποιείται ως βάση για νέα.
- Κατάσταση **Πρόχειρη** ή **Έτοιμη για αποστολή**.
- Άνοιγμα προ-συμπληρωμένου Gmail για τελική αποστολή από:
  `grand.secretary@nglgreece.gr`
- Η τελική αποστολή παραμένει ενέργεια του Μεγάλου Γραμματέα.
- Διαχείριση εγκεκριμένων χρηστών και δικαιωμάτων ανά πρότυπο.
- Login με email + OTP.
- Εκτύπωση ή αποθήκευση της τελικής επιστολής σε PDF από τον browser.

## Επίσημα στοιχεία

- **Οργανισμός:** Εθνική Μεγάλη Στοά της Ελλάδος
- **Έτος Ιδρύσεως:** 1986
- **Μέγας Διδάσκαλος:** Σεβτ. Αδ. Ιωάννης Μπενετάτος
- **Μεγάλος Γραμματέας:** Πανσεβ. Αδ. Δημήτριος Σκιαδόπουλος
- **Email αποστολής:** grand.secretary@nglgreece.gr

## Δομή εφαρμογής

```
letter-manager/
├── app.py
├── parts/
│   ├── 000.txt
│   ├── 001.txt
│   ├── 002.txt
│   ├── 003.txt
│   ├── 004.txt
│   ├── 005.txt
│   └── 006.txt
├── static/
│   ├── header_emblem.png.b64.*
│   ├── signature_original.png.b64.*
│   └── seal_original.png.b64.*
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env.example
└── README.md
```

Τα γραφικά αποθηκεύονται σε base64 text chunks και ανασυντίθενται δυναμικά από την εφαρμογή.

## Τοπική εκκίνηση

```bash
cd letter-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

export APP_SECRET='CHANGE_ME_TO_A_LONG_RANDOM_SECRET'
export ADMIN_EMAILS='grand.secretary@nglgreece.gr'
export DEV_SHOW_OTP='1'

uvicorn app:app --host 0.0.0.0 --port 8000
```

Στα Windows PowerShell:

```powershell
cd letter-manager
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

$env:APP_SECRET="CHANGE_ME_TO_A_LONG_RANDOM_SECRET"
$env:ADMIN_EMAILS="grand.secretary@nglgreece.gr"
$env:DEV_SHOW_OTP="1"

uvicorn app:app --host 0.0.0.0 --port 8000
```

## Παραγωγή / Live deployment

Το repository περιλαμβάνει έτοιμο `render.yaml` για deployment στο **Render**.

Το service χρησιμοποιεί Docker και persistent disk για τη βάση SQLite.

### Απαραίτητα environment variables

| Variable | Χρήση |
|---|---|
| `APP_SECRET` | Secret για τα signed sessions |
| `ADMIN_EMAILS` | Αρχικοί administrators |
| `COOKIE_SECURE` | Πρέπει να είναι `1` σε HTTPS |
| `DEV_SHOW_OTP` | Πρέπει να είναι `0` σε production |
| `DATA_DIR` | Persistent data directory, π.χ. `/var/data` |
| `SMTP_HOST` | SMTP server |
| `SMTP_PORT` | SMTP port, συνήθως 587 |
| `SMTP_USERNAME` | SMTP username |
| `SMTP_PASSWORD` | SMTP app password / secret |
| `OTP_FROM_EMAIL` | Email αποστολής OTP |

Για Google Workspace / Gmail, το `SMTP_PASSWORD` πρέπει να είναι **App Password** ή άλλο επιτρεπόμενο SMTP credential. Δεν πρέπει να αποθηκεύεται στο repository.

## Ασφάλεια

Σε production:

- `DEV_SHOW_OTP=0`
- `COOKIE_SECURE=1`
- χρήση ισχυρού `APP_SECRET`
- HTTPS
- SMTP credentials μόνο ως secrets του host
- τακτικό backup του persistent volume
- πρόσβαση μόνο σε εγκεκριμένα email
- απενεργοποίηση χρηστών που δεν χρειάζονται πλέον πρόσβαση

Η εφαρμογή προσθέτει επίσης βασικά security headers και `robots.txt` που αποτρέπει indexing.

## Βάση δεδομένων

Η εφαρμογή χρησιμοποιεί SQLite.

Default local path:

```
data/letters.db
```

Στο Render:

```
/var/data/letters.db
```

Το `/var/data` πρέπει να είναι persistent disk ώστε να μη χαθούν επιστολές και ρυθμίσεις σε νέο deploy.

## Health check

```
GET /health
```

Αναμενόμενη απάντηση:

```json
{
  "status": "ok",
  "service": "nglg-letter-manager"
}
```

## Ροή εργασίας

1. Ο διαχειριστής εγκρίνει το email ενός χρήστη.
2. Ο χρήστης εισάγει το email του.
3. Λαμβάνει OTP.
4. Επιλέγει επιτρεπόμενο πρότυπο.
5. Συμπληρώνει παραλήπτη, θέμα και κείμενο.
6. Η εφαρμογή εκδίδει νέο αριθμό πρωτοκόλλου.
7. Η επιστολή αποθηκεύεται στο αρχείο.
8. Γίνεται έλεγχος / διόρθωση.
9. Η επιστολή χαρακτηρίζεται «Έτοιμη για αποστολή».
10. Ανοίγει προ-συμπληρωμένο Gmail και η τελική αποστολή γίνεται από τον Μεγάλο Γραμματέα.

## Σημαντική σημείωση

Το **GitHub Pages δεν μπορεί να εκτελέσει** το FastAPI/Python backend ούτε την SQLite βάση.

Για αυτό η εφαρμογή πρέπει να φιλοξενείται σε platform που υποστηρίζει Docker/Python backend και persistent storage, όπως Render ή Railway.

---

**NGLG Letter Manager**  
Digital Secretariat System  
National Grand Lodge of Greece
