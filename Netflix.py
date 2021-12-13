import pandas as pd
import os
import matplotlib.pyplot as plt
import time

netflix_data_file = "d:/users/sebas/onedrive/repositories/netflix-repo/ViewingActivity.xlsx"
df = pd.read_excel(netflix_data_file)

df = df.drop(['Bookmark', 'Latest Bookmark', 'Country'], axis=1)

df['Start Time'] = pd.to_datetime(df['Start Time']) # zmiana formatu na datę
df['Duration'] = pd.to_timedelta(df['Duration']) # zmiana formatu na czas trwania

asia = df[df['Profile Name'].str.contains('Asia', regex=False)]
seeb = df[df['Profile Name'].str.contains('Seeb', regex=False)]
kuba = df[df['Profile Name'].str.contains('Kuba', regex=False)]
zetka = df[df['Profile Name'].str.contains('Zetka', regex=False)]


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
            new_df = df[df["Title"].str.contains(f'{movie_title}'.title(), case=False)]
            
            print()
            print(f'\n\n\t\tSumaryczny czas oglądania szukanego programów zawierających w tytule słowa "{movie_title}" wynosi:')
            print('\n\t\t===================')          
            print(f'\t\t  {new_df["Duration"].sum()}')
            print('\t\t===================')   
            input('\n\n\t\tEnter - dalej')
            watching_movies_time()   


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


def movie_time_by_user(user):
    clear_screen()

    while True:
        print('\n\n\t\tWpisz tytuł filmu lub serialu, którego czas oglądania chcesz poznać.')
        print(('\n\t\t0 - Powrót'))

        movie_title = input('\n\t\t\tTytuł: ')

        if movie_title == '0':
            user_analysis(user)
        else:
            if user == 'Asia':
                new_df = asia[df["Title"].str.contains(f'{movie_title}'.title(), case=False)]
            elif user == 'Seeb':
                new_df = seeb[df["Title"].str.contains(f'{movie_title}'.title(), case=False)]
            elif user == 'Kuba':
                new_df = kuba[df["Title"].str.contains(f'{movie_title}'.title(), case=False)]
            elif user == 'Zetka':
                new_df = zetka[df["Title"].str.contains(f'{movie_title}'.title(), case=False)]
            
            print()
            print(f'\n\n\t\tSumaryczny czas oglądania szukanego programów zawierających w tytule słowa "{movie_title}" wynosi:')
            print('\n\t\t===================')          
            print(f'\t\t  {new_df["Duration"].sum()}')
            print('\t\t===================')   
            input('\n\n\t\t\tEnter - dalej.')
            movie_time_by_user(user)


def device_type_by_user(user):
    clear_screen()

    print(f'\n\n\t\tSumaryczny czas oglądania Netflixa na poszczególnych urządzeniach przez użytkownika {user}.')
    print('\n\t\tW czasie między 29.10.2017 a 06.11.2021 do oglądania wykorzystano poniższe urządzenia:\n\n')

    device_type_list = list(df['Device Type'].drop_duplicates())
    
    for i in range(len(device_type_list)):

        device_df = df[df['Profile Name'].str.contains(f'{user}', regex=False)][df['Device Type'].str.contains(f'{device_type_list[i]}', regex=False)]
        print(f'\t\t{device_df["Duration"].sum()} -  {device_type_list[i]}')
    
    input('\n\nEnter - Dalej')
    user_analysis(user)


def most_least_watched(user):
    clear_screen()
    
    print(f'\n\n\t\tNajdłużej i najkrócej oglądane programy przez użytkownika {user}:')

    # can't create function - too many title differences, different seasons, different episode titles etc.
    
    input('\n\nEnter - Dalej')
    user_analysis(user)


def user_analysis(user):
    clear_screen()

    print(f'''
                        =====================
                          Netflix - {user}  
                        =====================
    ''')

    profile_total_duration = df[df['Profile Name'].str.contains(f'{user}', regex=False)]['Duration'].sum()

    print(f'\n\n\t\tCałkowity czas oglądania Netflix przez {user}:  {profile_total_duration}')
    print('\n\t\tDostępne informacje:')
    print('\n\t\t\t1 - Czas oglądania wybranego programu.')
    print('\t\t\t2 - Czas oglądania na poszczególnych urządzeniach.')
    print('\t\t\t3 - Najdłużej i najkrócej oglądane programy.')
    print('\n\t\t\t0 - Powrót')

    choice = input('\n\n\t\tTwój wybór :')

    if choice == '0':
        main_screen()
    elif choice == '1':
        movie_time_by_user(user)
    elif choice == '2':
        device_type_by_user(user)
    elif choice == '3':
        most_least_watched(user)
    else:
        print('\n\n\t\t\tBłędny wybór!')
        time.sleep(1)
        user_analysis(user)


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
        user_analysis('Asia')

    elif choice == '3':
        user_analysis('Kuba')

    elif choice == '4':
        user_analysis('Seeb')

    elif choice == '5':
        user_analysis('Zetka')
    
    elif choice == '0':
        print('\n\n\t\t\tDO ZOBACZENIA!\n\n')
        time.sleep(1)
        quit()
    
    else:
        print('\n\n\t\t\tBłędna opcja, powtórz wybór!')
        time.sleep(1)
        main_screen()


main_screen()