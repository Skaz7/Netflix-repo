import pandas as pd
import os
import matplotlib.pyplot as plt
import time

netflix_data_file = "d:/users/sebas/onedrive/repositories/netflix-repo/ViewingActivity.xlsx"
df = pd.read_excel(netflix_data_file)

# lista_danych = df.head(50).values.tolist() # lista składająca się jedynie z pierwszych 50 pozycji

df = df.drop(['Bookmark', 'Latest Bookmark', 'Country'], axis=1)


df['Start Time'] = pd.to_datetime(df['Start Time']) # zmiana formatu na datę
df['Duration'] = pd.to_timedelta(df['Duration']) # zmiana formatu na czas trwania


asia = df[df['Profile Name'].str.contains('Asia', regex=False)]
seeb = df[df['Profile Name'].str.contains('Seeb', regex=False)]
kuba = df[df['Profile Name'].str.contains('Kuba', regex=False)]
zetka = df[df['Profile Name'].str.contains('Zetka', regex=False)]


# print(seeb['Duration'].sum())
# print(kuba['Duration'].sum())
# print(zetka['Duration'].sum())
# print(asia['Duration'].sum())

# print()
# print(f'Asia zaczęła oglądać Netflix w dniu {min(asia["Start Time"])}')
# print()
# print(f'Asia ostani raz oglądała Netflix w dniu {max(asia["Start Time"])}')
# print()


def clear_screen():
    os.system('cls')


def summary_time():
    clear_screen()

    print(f'\n\n\t\tSumaryczny czas oglądania Netflixa przez wszyskich użytkowników wyniósł - {df["Duration"].sum()}')
    print('\n\t\tW tym:')
    print(f'\t\t\tAsia  - {asia["Duration"].sum()}')
    print(f'\t\t\tKuba  - {kuba["Duration"].sum()}')
    print(f'\t\t\tSeeb  - {seeb["Duration"].sum()}')
    print(f'\t\t\tZetka - {zetka["Duration"].sum()}\n\n')
    input('\n\n\n\tEnter - powrót.')
    general_analysis()


def watching_movies_time():
    clear_screen()

    while True:
        print('\n\n\t\tWpisz tytuł filmu lub serialu, którego czas oglądania chcesz poznać.')
        print(('\n\t\t0 - Powrót'))

        movie_title = input('\n\t\t\tTytuł: ')

        if movie_title == '0':
            general_analysis()
        else:
            new_df = df[df["Title"].str.contains(f'{movie_title}'.title(), case=False)] # creates new dataframe named '{movie_title}'
            
            print()
            print(f'\n\n\t\tSumaryczny czas oglądania szukanego programów zawierających w tytule słowa "{movie_title}" wynosi:')
            print('\n\t\t===================')          
            print(f'\t\t  {new_df["Duration"].sum()}')
            print('\t\t===================')   
            continue   


def device_type():
    clear_screen()

    print('\n\n\t\tSumaryczny czas oglądania Netflixa na poszczególnych urządzeniach.')
    print('\n\t\tW czasie między 29.10.2017 a 06.11.2021 do oglądania wykorzystano poniższe urządzenia:\n')

    device_type_list = list(df['Device Type'].drop_duplicates())
    
    for i in range(len(device_type_list)):
        print(f'\t\t\t{i+1}. {device_type_list[i]}')
    
    print('\n\t\t\t0 - Powrót')

    try:
        choice = int(input('\n\n\t\tTwój wybór: '))

        if choice == 0:
            general_analysis()

        elif choice < 0 or choice > len(device_type_list):
            print('\n\n\t\t\t\tBłędny wybór, powtórz!')
            time.sleep(1)
            device_type()
        
        else:
            device_df = df[df['Device Type'].str.contains(f'{device_type_list[choice - 1]}', regex=False)]
            print(f'\n\t\tCzas oglądania Netflixa na urządzeniu "{device_type_list[choice - 1]}" wynosi:  {device_df["Duration"].sum()}')

            input('\n\nEnter - Dalej')
            device_type()

    except ValueError:
        print(f'\n\n\t\t\tMusisz wybrać liczbę z zakresu 1 - {len(device_type_list)}')
        time.sleep(1)
        device_type()


def general_analysis():
    clear_screen()

    print('\n\n\t\t=================================================================================')
    print('\n\t\tJakie informacje chcesz uzyskać?')
    print('\n\t\t\t1 - Sumaryczny czas oglądania Netflixa przez poszczególnych użytkowników.')
    print('\t\t\t2 - Łączny czas oglądania wybranych tytułów przez wszyskich użytkowników.')
    print('\t\t\t3 - Czas oglądania na poszczególnych urządzeniach.')
    print('\n\t\t\t0 - Powrót.')
    print('\n\t\t=================================================================================')

    choice = input('\n\n\t\tTwój wybór :  ')

    if choice == '1':
        summary_time()
    elif choice == '2':
        watching_movies_time()
    elif choice == '3':
        device_type()
    elif choice == '0':
        main_screen()


def asia_analysis():
    pass


def kuba_analysis():
    pass


def seeb_analysis():
    pass


def zuzia_analysis():
    pass


def main_screen():
    clear_screen()

    print('\n\n\t\t================================')
    print('\n\t\tJakie dane chcesz wyświetlić? :')
    print('\n\t\t\t1 - Ogólne')
    print('\t\t\t2 - Asia')
    print('\t\t\t3 - Kuba')
    print('\t\t\t4 - Seeb')
    print('\t\t\t5 - Zuzia')
    print('\n\t\t\t0 - Wyście z programu')
    print('\n\t\t================================')

    choice = input('\n\n\t\tTwój wybór :  ')

    if choice == '1':
        general_analysis()

    elif choice == '2':
        asia_analysis()

    elif choice == '3':
        kuba_analysis()

    elif choice == '4':
        seeb_analysis()

    elif choice == '5':
        zuzia_analysis()
    
    elif choice == '0':
        print('\n\n\t\t\tDO ZOBACZENIA!\n\n')
        time.sleep(1)
        quit()
    
    else:
        print('\n\n\t\t\tBłędna opcja, powtórz wybór!')
        time.sleep(1)
        main_screen()


main_screen()