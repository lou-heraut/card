// Filtrage du catalogue, côté navigateur.
//
// Ce script n'implémente AUCUNE logique de corpus : le tableau entier est
// écrit à la construction par scripts/generate_catalog.py, depuis
// card.list_cards(). Il ne fait que masquer des lignes déjà présentes,
// donc il ne peut pas dire autre chose que le paquet, et la page reste
// lisible sans lui : moteurs de recherche, lecteurs d'écran, JS coupé.
(function () {
  var table = document.getElementById("cat-table");
  if (!table) return;

  var q = document.getElementById("cat-q");
  var lang = document.getElementById("cat-lang");
  var reset = document.getElementById("cat-reset");
  var shown = document.getElementById("cat-shown");
  var selects = [].slice.call(document.querySelectorAll("[data-facet]"));
  var rows = [].slice.call(table.tBodies[0].rows);

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

    for (var i = 0; i < rows.length; i++) {
      var ligne = rows[i], ok = true;
      for (var j = 0; ok && j < actifs.length; j++) {
        ok = porte(ligne, actifs[j].dataset.facet, actifs[j].value);
      }
      if (ok && mots.length) {
        var hay = ligne.getAttribute("data-search") || "";
        for (var k = 0; ok && k < mots.length; k++) {
          ok = hay.indexOf(mots[k]) !== -1;
        }
      }
      ligne.hidden = !ok;
      if (ok) n++;
    }
    shown.textContent = n;
  }

  function langue() {
    table.classList.toggle("show-fr", lang.value === "fr");
    // La préférence suit le visiteur d'une page à l'autre. Si le stockage
    // est refusé (navigation privée stricte), on n'insiste pas.
    try { localStorage.setItem("card-lang", lang.value); } catch (e) {}
  }

  try {
    var memo = localStorage.getItem("card-lang");
    if (memo) { lang.value = memo; }
  } catch (e) {}

  q.addEventListener("input", filtre);
  selects.forEach(function (s) { s.addEventListener("change", filtre); });
  lang.addEventListener("change", langue);
  reset.addEventListener("click", function () {
    q.value = "";
    selects.forEach(function (s) { s.value = ""; });
    filtre();
    q.focus();
  });

  langue();
  filtre();
})();
