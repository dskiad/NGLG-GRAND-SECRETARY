# NGLG Letter Manager — Ψηφιακή Μεγάλη Γραμματεία

Web εφαρμογή της Μεγάλης Γραμματείας για γρήγορη δημιουργία, πρωτοκόλληση, αρχειοθέτηση και επαναχρησιμοποίηση επίσημων επιστολών.

## Περιλαμβάνει
- αυτόματο αριθμό πρωτοκόλλου ανά έτος και αυτόματη ημερομηνία,
- σταθερό επίσημο επιστολόχαρτο με έμβλημα, υπογραφή και σφραγίδα,
- θέμα, παραλήπτη, email και κείμενο επιστολής,
- πρότυπα ανά περίπτωση (Επίσκεψη ΜΔ, Επίσκεψη ΜΔ με εκπρόσωπο, Συλλυπητήρια κ.ά.),
- αρχείο με αναζήτηση κατά πρωτόκολλο, θέμα, ημερομηνία ή παραλήπτη,
- «Νέα πάνω σε αυτή» για δημιουργία νέου εγγράφου από παλαιό,
- εγκεκριμένους χρήστες με email + OTP και δικαιώματα ανά πρότυπο,
- κατάσταση «Έτοιμη για αποστολή» και άνοιγμα προ-συμπληρωμένου Gmail από `grand.secretary@nglgreece.gr`· η τελική αποστολή γίνεται από τον Μεγάλο Γραμματέα.

Τα τρία γραφικά αποθηκεύονται ως `.b64` text assets ώστε το repository να μεταφέρεται εύκολα μέσω του GitHub API.

## Εκκίνηση
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export APP_SECRET='βάλε-ισχυρό-secret'
export ADMIN_EMAILS='grand.secretary@nglgreece.gr'
uvicorn app:app --host 0.0.0.0 --port 8000
```

Για πραγματικό OTP ρυθμίστε τα SMTP variables του `.env.example` και σε παραγωγή οπωσδήποτε `DEV_SHOW_OTP=0`, HTTPS και ασφαλές `APP_SECRET`.

Η SQLite βάση είναι στο `data/letters.db`. Σε production host απαιτείται persistent volume για το `data/`.

> Το GitHub Pages δεν εκτελεί FastAPI/Python backend. Για live χρήση χρειάζεται Render, Railway, Fly.io, VPS ή άλλο Python/Docker host.
