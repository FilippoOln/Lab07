import flet as ft

from UI.alert import AlertManager
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN

    def popola_ddB_e_ddG(self):
        self._view._ddB.options.append(ft.dropdown.Option("Nessun filtro"))
        self._view._ddG.options.append(ft.dropdown.Option("Nessun filtro"))
        biblioteche = self._model.get_biblioteche()
        generi = self._model.get_generi()
        if biblioteche is not None and generi is not None:
            for b in biblioteche:
                self._view._ddB.options.append(ft.dropdown.Option(b.nome))
            for genere in generi:
                self._view._ddG.options.append(ft.dropdown.Option(genere))

        else:
            # Non è stato possibile connettersi al db per caricare le biblioteche e/o i generi
            self._view.show_alert(f"❌ Errore nel caricamento delle biblioteche e/o dei generi dal db")
        self._view.update()

    # CALLBACKS DROPDOWN
    def handler_aggiorna_biblioteca(self, e):
        if self._view._ddB.value == "Nessun filtro":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = self._view._ddB.value

    def handler_aggiorna_genere(self, e):
        if self._view._ddG.value == "Nessun filtro":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = self._view._ddG.value

    # AZIONE: MOSTRA LIBRI
    def handler_mostra_libri(self, e):
        self._view._list_view.controls.clear()
        libri_filtrati = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        if libri_filtrati is not None:
            if len(libri_filtrati) == 0:
                self._view.show_alert(f"❌ Nessun libro trovato!!")
            else:
                for libro in libri_filtrati:
                    self._view._list_view.controls.append(ft.Text(f"{libro}"))
        else:
            self._view.show_alert(f"❌ Non è stato possibile connetersi al database")
        self._view.update()

