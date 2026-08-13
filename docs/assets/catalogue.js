// Le catalogue, côté navigateur : la langue, le filtre, l'adresse.
//
// Ce script n'implémente AUCUNE logique de corpus. Les entrées sont
// écrites à la construction par scripts/generate_catalog.py, depuis
// card.list_cards(), et il ne fait que les masquer : il ne peut donc pas
// dire autre chose que le paquet. Le dépliage lui échappe complètement,
// c'est celui de <details>. Sans lui la page reste entière : moteurs de
// recherche, lecteurs d'écran, JS coupé.

// ── 1. la langue, sur TOUTES les pages ────────────────────────────────
// Une seule bascule pour le site : la classe est posée sur <body> et le
// CSS masque ce qui porte l'autre langue, que ce soit un nom dans une
// liste ou la figure entière d'une fiche.
(function () {
  var memo = null;
  try { memo = localStorage.getItem("card-lang"); } catch (e) {}

  function applique(lang) {
    document.body.classList.toggle("show-fr", lang === "fr");
    try { localStorage.setItem("card-lang", lang); } catch (e) {}
  }

  var select = document.getElementById("cat-lang");
  if (memo && select) { select.value = memo; }
  if (memo) { applique(memo); }
  if (select) {
    select.addEventListener("change", function () { applique(select.value); });
  }
})();


// ── 2. le filtre, sur la page catalogue ───────────────────────────────
(function () {
  var liste = document.getElementById("cat-list");
  if (!liste) return;

  var q = document.getElementById("cat-q");
  var reset = document.getElementById("cat-reset");
  var vues = document.getElementById("cat-shown");
  var selects = [].slice.call(document.querySelectorAll("[data-facet]"));
  var lignes = [].slice.call(liste.querySelectorAll(".cat-row"));
  // Ce qu'on cherche est le texte de l'entrée elle-même, relevé une fois
  // au chargement : symboles, noms et description, dans les DEUX langues,
  // qu'une seule soit affichée ou non. Le recopier dans un attribut à la
  // construction aurait été une seconde version du même texte.
  var foin = lignes.map(function (l) {
    return (l.textContent || "").toLowerCase().replace(/\s+/g, " ");
  });
  // La famille n'a pas de menu : elle vient d'un lien « toutes les
  // variantes » et ne se choisit pas dans le vide, un slug de famille
  // n'étant pas quelque chose qu'on tape.
  var famille = "";

  // Une facette multi-valeurs porte ses slugs séparés par une espace :
  // `domain="flow precipitation"` doit répondre au filtre `flow`.
  function porte(ligne, facette, valeur) {
    var v = ligne.getAttribute("data-" + facette) || "";
    return (" " + v + " ").indexOf(" " + valeur + " ") !== -1;
  }

  function filtre() {
    var texte = (q.value || "").trim().toLowerCase();
    // Chaque mot doit être présent, dans n'importe quel ordre : on tape
    // « annuel minimum » sans se demander comment la phrase est tournée.
    var mots = texte ? texte.split(/\s+/) : [];
    var actifs = selects.filter(function (s) { return s.value; });
    var n = 0;

    for (var i = 0; i < lignes.length; i++) {
      var ligne = lignes[i], ok = true;
      if (famille) { ok = ligne.getAttribute("data-family") === famille; }
      for (var j = 0; ok && j < actifs.length; j++) {
        ok = porte(ligne, actifs[j].dataset.facet, actifs[j].value);
      }
      if (ok && mots.length) {
        for (var k = 0; ok && k < mots.length; k++) {
          ok = foin[i].indexOf(mots[k]) !== -1;
        }
      }
      ligne.hidden = !ok;
      if (ok) n++;
    }
    vues.textContent = n;
    ecrit_adresse();
  }

  // L'état du filtre vit dans l'ADRESSE : une vue filtrée s'envoie par
  // courriel, se met en signet et se cite. Sans ça, « les basses eaux
  // annuelles » n'est pas quelque chose qu'on peut montrer à quelqu'un.
  function ecrit_adresse() {
    var p = new URLSearchParams();
    if (q.value.trim()) { p.set("q", q.value.trim()); }
    selects.forEach(function (s) {
      if (s.value) { p.set(s.dataset.facet, s.value); }
    });
    if (famille) { p.set("family", famille); }
    var suite = p.toString();
    history.replaceState(null, "",
      location.pathname + (suite ? "?" + suite : "") + location.hash);
  }

  function lit_adresse() {
    var p = new URLSearchParams(location.search);
    if (p.get("q")) { q.value = p.get("q"); }
    selects.forEach(function (s) {
      var v = p.get(s.dataset.facet);
      if (v) { s.value = v; }
    });
    famille = p.get("family") || "";
  }

  // Une entrée visée par l'adresse (#VCN10) s'ouvre et se montre : une
  // ancre qui tombe sur un bloc replié ne sert à rien.
  function ouvre_visee() {
    if (!location.hash) return;
    var cible = document.getElementById(
      decodeURIComponent(location.hash.slice(1)));
    if (cible && cible.classList.contains("cat-row")) {
      cible.open = true;
      cible.hidden = false;
      cible.scrollIntoView({ block: "center" });
    }
  }

  q.addEventListener("input", filtre);
  selects.forEach(function (s) {
    s.addEventListener("change", function () { famille = ""; filtre(); });
  });
  reset.addEventListener("click", function () {
    q.value = "";
    famille = "";
    selects.forEach(function (s) { s.value = ""; });
    filtre();
    q.focus();
  });
  window.addEventListener("hashchange", ouvre_visee);

  lit_adresse();
  filtre();
  ouvre_visee();
})();
