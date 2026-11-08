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
    def popola_ddB(self):
        self._view._ddB.options.append(ft.dropdown.Option("Nessun filtro"))
        biblioteche = self._model.get_biblioteche()
        # se la funzione restituisce None significa che la connessione non è andata a buon fine
        if biblioteche is not None:
            if len(biblioteche) == 0:
                self._view.show_alert(f"❌ Errore nel caricamento delle biblioteche dal database!")
            else:
                for b in biblioteche:
                    self._view._ddB.options.append(ft.dropdown.Option(b.nome))

        else:
            self._view.show_alert(f"❌ Non è stato possibile connetersi al database")
        self._view.update()


    def popola_ddG(self):
        self._view._ddG.options.append(ft.dropdown.Option("Nessun filtro"))
        generi = self._model.get_generi()
        if generi is not None:
            if len(generi) == 0:
                self._view.show_alert(f"❌ Errore nel caricamento dei generi dal database!")
            else:
                for genere in generi:
                    self._view._ddG.options.append(ft.dropdown.Option(genere))
        else:
            self._view.show_alert(f"❌ Non è stato possibile connetersi al database")
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

