import json as js
import sys
import requests
from datetime import date
import os
import operator


class DataLoad:

    def __init__(self):
        self.date = str(date.today())
        self.path_api = "https://archive.scryfall.com/json/scryfall-default-cards.json"
        self.data_path = sys.path[0] + "/Data/Card_Database_"+self.date+".json"

        self.pop_array = ['name', 'png', 'cmc', 'type_line', 'color_identity', 'layout']
        self.toxic_layouts = ['art_series', 'double_faced_token', 'planar', 'emblem', 'token', 'scheme', 'vanguard',
                              'augment', 'host']
        self.stupid_melds = ['Brisela, Voice of Nightmares', 'Hanweir, the Writhing Township', 'Chittering Host']
        self.start()

    def start(self):
        counter = 0
        string_name = ' '
        for file in os.listdir(sys.path[0]+"/Data"):
            if file.endswith('.json') == True:
                counter +=1
                string_name = str(file)
        if counter > 1 or counter == 0:
            self.del_down_sort()
        elif self.check_deltatime(string_name) == True:
            self.del_down_sort()
        else:
            self.data_path = string_name
            print('No new download was necessary.')


    def del_down_sort(self):
        self.delete_all_json()
        self.download_json()
        self.perfect_json()


    def check_deltatime(self, stro):
        stro = stro[-15:-5:1]
        date_stamp = date(int(stro[0:4]), int(stro[5:7]), int(stro[8:10]))
        delta_time = date.today() - date_stamp
        if delta_time.days >= 20:
            return True
        else:
            return False


    def download_json(self):
        response = requests.get(self.path_api)
        print(response.status_code)
        with open(self.data_path, 'wb') as f:
            f.write(response.content)
        print('New file downloaded')


    def delete_all_json(self):
        for file in os.listdir(sys.path[0]+"/Data"):
            if file.endswith(".json"):
                string = os.path.join(sys.path[0]+"/Data", file)
                os.remove(string)
                print('File: ' + string + " was deleted")


    def perfect_json(self):
        with open(self.data_path) as js_file:
            data = js.load(js_file)

        beginning_length = len(data)
        watch_counter = 0

        while watch_counter != beginning_length:
            png_arr = []
            if data[watch_counter]['layout'] in self.toxic_layouts or (
                    data[watch_counter]['layout'] == 'meld' and data[watch_counter]['name'] in self.stupid_melds):
                data.pop(watch_counter)
                beginning_length = len(data)
            else:
                try:
                    if data[watch_counter]['layout'] == 'transform':
                        array_both = [data[watch_counter]['card_faces'][0]['image_uris']['png']]
                        png_data = data[watch_counter]['card_faces'][1]['image_uris']['png']
                        array_both.append(png_data)
                        png_arr.append(array_both)
                    else:
                        png_arr.append(data[watch_counter]['image_uris']['png'])
                    data[watch_counter]['png'] = png_arr
                except:
                    print(data[watch_counter])

                delete_list = []

                for part in data[watch_counter]:
                    if part not in self.pop_array:
                        delete_list.append(part)

                for i in range(0, len(delete_list)):
                    data[watch_counter].pop(delete_list[i])
                watch_counter += 1
        data.sort(key=operator.itemgetter('name'))
        self.combine(data)


        with open(self.data_path, 'w') as outfile:
            js.dump(data, outfile)


    def combine(self, data):
        watch_counter = 0
        length = len(data)
        while watch_counter != length:
            try:
                if data[watch_counter]['name'] == data[watch_counter+1]['name']:
                    if data[watch_counter]['layout'] == 'transform':
                        data[watch_counter]['png'].append(data[watch_counter+1]['png'])
                    else:
                        data[watch_counter]['png'].append(data[watch_counter+1]['png'][0])
                    data.pop(watch_counter+1)
                else:
                    watch_counter += 1
                    length = len(data)

            except:
                print('finished')
                break



text = False
if text == True:

    print('Laden der Bilder bei der ersten Erstellung des Cubes')

    # Erschaffen von Archetypen

    # Benötige ein Ordner mit den heruntergeladenen Bildern des Cubes, damit eine Offline Version verfügbar ist
    # Iwo müssen die Archetypes festgehalten werden
    # Benötige ein Array mit Kartenname, Kartentyp, Kartenfarbe, Manakosten, Archetyp, Path_picture

    # Suche nach einer Karte beginnend mit Kartenname (Meta-Daten-Suche ist iwann ein upgrade, s. Scryfall), gesucht wird im
    # kompletten Json-Arbeits-File
    # --> bei Auffinden der Karte, platzieren in dem Array, Download des Bildes (+bennenen), falls noch nicht im Bilderordner (beides
    # sortieren nach Namen)
    # --> zeitgleiches zuordnen von Archetypes

    # bei Beenden des Arbeitsvorganges, speichern des Arrays in beliebiger Form

    print('Laden des Arrays mit den Karten eines Cubes')
    # Auslesen der Speicherung des Arrays in Arbeitsspeicher

    print('Weitere Bearbeitung des Cubes nach Beenden der ersten Erstellung, gleiches Layout')

    print('Anzeigen des gesamten Cubes in Kartennamen für Farben, nach Typ vgl. Cubetutor')
