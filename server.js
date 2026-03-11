'use strict';

const express = require('express');
const path    = require('path');
const fs      = require('fs');

const app  = express();
const PORT = process.env.PORT || 5000;

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({ extended: false }));

// ── Exercise logic ────────────────────────────────────────────────────────────

// 6.1 reklaam
function banner(sisu) {
  return sisu.toUpperCase();
}

// 6.2 teler
function teleriDiagonaal(kaugus) {
  return Math.round(kaugus * 100 * 0.39 / 2.5);
}

// 6.3 pidu
function eelarve(guests) {
  return guests * 10 + 55;
}

// 6.4a mitmes
function tervitus(mitmes) {
  return (
    'Võõrustaja: "Tere!"\n' +
    'Täna ' + mitmes + '. kord tervitada, mõtiskleb võõrustaja.\n' +
    'Külaline: "Tere, suur tänu kutse eest!"'
  );
}

// 6.4b myndid
function pronksikarvasSumma(failinimi) {
  const absPath = path.resolve(__dirname, failinimi);
  if (!absPath.startsWith(__dirname + path.sep)) {
    throw new Error('Keelatud failinimi');
  }
  const raw   = fs.readFileSync(absPath, 'utf8');
  let summa   = 0;
  for (const rida of raw.split('\n')) {
    const trimmed = rida.trim();
    if (trimmed === '') continue;
    const val = parseInt(trimmed, 10);
    if (val <= 5) summa += val;
  }
  return summa;
}

// 6.4c kuupaev
function kuuNimi(kuuNumber) {
  const kuuNimed = [
    'jaanuar', 'veebruar', 'märts', 'aprill',
    'mai', 'juuni', 'juuli', 'august',
    'september', 'oktoober', 'november', 'detsember'
  ];
  return kuuNimed[kuuNumber - 1];
}

function kuupaevSonena(kuupaev) {
  const osad = kuupaev.split('.');
  return osad[0] + '. ' + kuuNimi(parseInt(osad[1], 10)) + ' ' + osad[2] + '. a';
}

// ── Routes ────────────────────────────────────────────────────────────────────

app.get('/', (req, res) => {
  res.render('index');
});

// 6.1 reklaam
app.get('/reklaam', (req, res) => {
  res.render('reklaam', { tulemus: null });
});
app.post('/reklaam', (req, res) => {
  const mitu    = parseInt(req.body.mitu, 10);
  const sisu    = req.body.sisu;
  const tulemus = Array.from({ length: mitu }, () => banner(sisu)).join('\n');
  res.render('reklaam', { tulemus });
});

// 6.2 teler
app.get('/teler', (req, res) => {
  res.render('teler', { tulemus: null });
});
app.post('/teler', (req, res) => {
  const kaugus  = parseFloat(req.body.kaugus);
  const tulemus = teleriDiagonaal(kaugus) + ' tolli';
  res.render('teler', { tulemus });
});

// 6.3 pidu
app.get('/pidu', (req, res) => {
  res.render('pidu', { tulemus: null });
});
app.post('/pidu', (req, res) => {
  const guests  = parseInt(req.body.guests, 10);
  const yes     = parseInt(req.body.yes, 10);
  const tulemus = 'Maksimaalne eelarve: ' + eelarve(guests) + '\n' +
                  'Minimaalne eelarve: ' + eelarve(yes);
  res.render('pidu', { tulemus });
});

// 6.4a mitmes
app.get('/mitmes', (req, res) => {
  res.render('mitmes', { tulemus: null });
});
app.post('/mitmes', (req, res) => {
  const arv  = parseInt(req.body.arv, 10);
  const read = [];
  for (let i = 1; i <= arv; i++) {
    read.push(tervitus(i));
  }
  const tulemus = read.length > 0 ? read.join('\n') : null;
  res.render('mitmes', { tulemus });
});

// 6.4b myndid
app.get('/myndid', (req, res) => {
  res.render('myndid', { tulemus: null });
});
app.post('/myndid', (req, res) => {
  const failinimi = (req.body.failinimi || 'myndid.txt').trim();
  try {
    const summa   = pronksikarvasSumma(failinimi);
    const tulemus = 'Pronksikarva müntide summa: ' + summa + ' senti';
    res.render('myndid', { tulemus });
  } catch (err) {
    res.render('myndid', { tulemus: 'Viga: faili ei leitud – ' + failinimi });
  }
});

// 6.4c kuupaev
app.get('/kuupaev', (req, res) => {
  res.render('kuupaev', { tulemus: null });
});
app.post('/kuupaev', (req, res) => {
  const tulemus = kuupaevSonena(req.body.kuupaev);
  res.render('kuupaev', { tulemus });
});

// ── Start ─────────────────────────────────────────────────────────────────────
app.listen(PORT, '0.0.0.0', () => {
  console.log('Server töötab aadressil http://0.0.0.0:' + PORT);
});
