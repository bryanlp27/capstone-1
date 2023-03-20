isiData={
    '56321':{
    'No BPJS Pasien':'56321',    
    'Nama Pasien':'Tommy Haryanto',    
    'Usia':'38',    
    'Gender':'Pria',    
    'Penyakit':'Demam'    
    },
    '74521':{
    'No BPJS Pasien':'74521',    
    'Nama Pasien':'Elizabeth Sugigi',    
    'Usia':'26',    
    'Gender':'Wanita',    
    'Penyakit':'AIDS'    
    },
    '98932':{
    'No BPJS Pasien':'98932',    
    'Nama Pasien':'Frans Mahardika',    
    'Usia':'17',    
    'Gender':'Pria',    
    'Penyakit':'Bronkitis'    
    },
    '27481':{
    'No BPJS Pasien':'27481',    
    'Nama Pasien':'Cut Meyrizki',    
    'Usia':'21',    
    'Gender':'Wanita',    
    'Penyakit':'Tetanus'    
    },
    '66425':{
    'No BPJS Pasien':'66425',    
    'Nama Pasien':'Parker Taylor',    
    'Usia':'44',    
    'Gender':'Pria',    
    'Penyakit':'Cacar'    
    }
}

# Menu Utama
def beranda():
    print('\n===========================================')
    print('      Aplikasi Rumah Sehat Rastamania      ')
    print('===========================================')
    print('\nMenu Aplikasi :')
    print('\n1. Menampilkan Data Pasien')
    print('2. Menambahkan Data Pasien')
    print('3. Update Data Pasien')
    print('4. Hapus Data Pasien')
    print('5. Exit\n')


    inputUser=input('Masukkan Pilihan Menu : ')

    if inputUser=='1':
        tampilData()
    elif inputUser=='2':
        tambahData()
    elif inputUser=='3':
        updateData()
    elif inputUser=='4':
        hapusData()
    elif inputUser=='5':
        keluar()
    else:
        print('Pilihan yang Anda Masukkan Salah!')
        beranda()

# Menu Tampil / Read Data
def tampilData():
    print('\n===========================================')
    print('Menu Menampilkan Data Pasien')
    print('===========================================')
    print('\n1. Cek Data Pasien')
    print('2. Tampil Input Data Pasien')
    print('3. Kembali ke Beranda')

    inputUser=input('\nMasukkan Pilihan Menu : ')
    
    if inputUser=='1':
        cekDataPasien()
    elif inputUser=='2':
        tampilInputDataPasien()
    elif inputUser=='3':
        beranda()
    else:
        print('\nPilihan yang Anda Masukkan Salah!')
        tampilData()
        
def cekDataPasien():
    if len(isiData)==0:
        print('\nTidak Ada Data!')
        tampilData()
    else:
        print('\nNo BPJS Pasien \t|Nama Pasien \t\t\t|Usia \t\t|Gender \t\t|Penyakit')
        for i,j in isiData.items():
            print(f'{isiData[i]["No BPJS Pasien"]} \t\t|{isiData[i]["Nama Pasien"]}   \t\t|{isiData[i]["Usia"]} \t\t|{isiData[i]["Gender"]}    \t\t|{isiData[i]["Penyakit"]}')
        tampilData()  

def tampilInputDataPasien():
    if len(isiData)==0:
        print('\nTidak Ada Data!')
        tampilData()
    else:
        inputUser=input('\nMasukkan No BPJS Pasien : ')
        if inputUser in isiData:
            print('\nNo BPJS Pasien \t|Nama Pasien \t\t\t|Usia \t\t|Gender \t\t|Penyakit')
            print(f'{isiData[inputUser]["No BPJS Pasien"]} \t\t|{isiData[inputUser]["Nama Pasien"]}   \t\t|{isiData[inputUser]["Usia"]} \t\t|{isiData[inputUser]["Gender"]}    \t\t|{isiData[inputUser]["Penyakit"]}')
            tampilData()
        else:
            print('\nTidak Ada Data!')
            tampilData()
        
# Menu Tambah / Create Data 
def tambahData():
    print('\n===========================================')
    print('Menu Menambahkan Data Pasien')
    print('===========================================')
    print('\n1. Tambahkan Data Pasien')
    print('2. Kembali ke Beranda')
    
    inputUser=input('\nMasukkan Pilihan Menu : ')
    
    if inputUser=='1':
        tambahDataPasien()
    elif inputUser=='2':
        beranda()
    else:
        tambahData()
        
def tambahDataPasien():
    inputUser=input('\nMasukkan No BPJS Pasien : ')
    if inputUser in isiData:
        print('\nData Sudah Ada!')
        tambahData()
    else:
        inputNamaPasien=input('Masukkan Nama Pasien : ')
        inputUsiaPasien=input('Masukkan Usia Pasien : ')
        inputGenderPasien=input('Masukkan Gender Pasien : ')
        inputPenyakitPasien=input('Masukkan Penyakit Pasien : ')
        
        print('\nNo BPJS Pasien \t|Nama Pasien \t\t\t\t|Usia \t\t|Gender \t\t|Penyakit')
        print(f'{inputUser} \t\t|{inputNamaPasien} \t\t\t|{inputUsiaPasien} \t\t|{inputGenderPasien} \t\t\t|{inputPenyakitPasien}')
        
        print('\nSimpan Data Pasien?')
        print('1. Ya')
        print('2. Tidak')
        inputSimpanData=input('\nPilih Menu (1/2) : ')
        
        if inputSimpanData=='1':
            dataLokal={
                'No BPJS Pasien':inputUser,    
                'Nama Pasien':inputNamaPasien,    
                'Usia':inputUsiaPasien,    
                'Gender':inputGenderPasien,    
                'Penyakit':inputPenyakitPasien
            }
            isiData[inputUser]=dataLokal
            print('Data Tersimpan!')
            tambahData()
        elif inputSimpanData=='2':
            tambahData()

# Menu Update Data
def updateData():
    print('\n===========================================')
    print('Menu Update Data Pasien')
    print('===========================================')
    print('\n1. Update Data Pasien')
    print('2. Kembali ke Beranda')

    inputUser=input('\nMasukkan Pilihan Menu : ')
    
    if inputUser=='1':
        updateDataPasien()
    elif inputUser=='2':
        beranda()
    else:
        updateData()

def updateDataPasien():
    inputUser=input('\nMasukkan No BPJS Pasien : ')
    if not inputUser in isiData:
        print('\nData yang Anda Cari Tidak Ada!')
        updateData()
    elif inputUser in isiData:
        print('\nNo BPJS Pasien \t|Nama Pasien \t\t|Usia \t\t|Gender \t|Penyakit')
        print(f'{isiData[inputUser]["No BPJS Pasien"]} \t\t|{isiData[inputUser]["Nama Pasien"]}   \t|{isiData[inputUser]["Usia"]} \t\t|{isiData[inputUser]["Gender"]}    \t|{isiData[inputUser]["Penyakit"]}')
        
        print('\nLanjut Update Data Pasien?')
        print('1. Ya')
        print('2. Tidak')
        
        inputLanjutUpdateData=input('\nPilih Menu (1/2) : ')
    
        if inputLanjutUpdateData=='1':
            
            print('\nPilih Data Pasien yang akan di Update : ')
            print('1. No BPJS Pasien')
            print('2. Nama Pasien')
            print('3. Usia Pasien')
            print('4. Gender Pasien')
            print('5. Penyakit Pasien')
            
            inputPilihanMenuUpdateData=input('\nPilih Menu (1-5) : ')
            
            if inputPilihanMenuUpdateData=='1':
                
                inputNoBPJSPasienBaru=input('Masukkan No BPJS Pasien Terbaru : ')
                
                print('\nYakin Update Data Pasien?')
                print('1. Ya')
                print('2. Tidak')
                
                inputYakinUpdateData=input('\nPilih Menu (1/2) : ')
                
                if inputYakinUpdateData=='1':
                    isiData[inputUser]['No BPJS Pasien']=inputNoBPJSPasienBaru
                    isiData[inputNoBPJSPasienBaru]=isiData[inputUser]
                    del isiData[inputUser]
                    print('\nData Telah Terupdate!')
                    updateData()
                elif inputYakinUpdateData=='2':
                    updateData()
                else:
                    updateData()
                
            elif inputPilihanMenuUpdateData=='2':
                
                inputNamaPasienBaru=input('Masukkan Nama Pasien Terbaru : ')
                
                print('\nYakin Update Data Pasien?')
                print('1. Ya')
                print('2. Tidak')
                
                inputYakinUpdateData=input('\nPilih Menu (1/2) : ')
                
                if inputYakinUpdateData=='1':
                    isiData[inputUser]['Nama Pasien']=inputNamaPasienBaru
                    print('\nData Telah Terupdate!')
                    updateData()
                elif inputYakinUpdateData=='2':
                    updateData()
                else:
                    updateData()
                
            elif inputPilihanMenuUpdateData=='3':
                
                inputUsiaPasienBaru=input('Masukkan Usia Pasien Terbaru : ')
                
                print('\nYakin Update Data Pasien?')
                print('1. Ya')
                print('2. Tidak')
                
                inputYakinUpdateData=input('\nPilih Menu (1/2) : ')
                
                if inputYakinUpdateData=='1':
                    isiData[inputUser]['Usia']=inputUsiaPasienBaru
                    print('\nData Telah Terupdate!')
                    updateData()
                elif inputYakinUpdateData=='2':
                    updateData()
                else:
                    updateData()
            
            elif inputPilihanMenuUpdateData=='4':
            
                inputGenderPasienBaru=input('Masukkan Gender Pasien Terbaru : ')
                
                print('\nYakin Update Data Pasien?')
                print('1. Ya')
                print('2. Tidak')
                
                inputYakinUpdateData=input('\nPilih Menu (1/2) : ')
                
                if inputYakinUpdateData=='1':
                    isiData[inputUser]['Gender']=inputGenderPasienBaru
                    print('\nData Telah Terupdate!')
                    updateData()
                elif inputYakinUpdateData=='2':
                    updateData()
                else:
                    updateData()
            
            elif inputPilihanMenuUpdateData=='5':
            
                inputPenyakitPasienBaru=input('Masukkan Penyakit Pasien Terbaru : ')
                
                print('\nYakin Update Data Pasien?')
                print('1. Ya')
                print('2. Tidak')
                
                inputYakinUpdateData=input('\nPilih Menu (1/2) : ')
                
                if inputYakinUpdateData=='1':
                    isiData[inputUser]['Penyakit']=inputPenyakitPasienBaru
                    print('\nData Telah Terupdate!')
                    updateData()
                elif inputYakinUpdateData=='2':
                    updateData()
                else:
                    updateData()
            
            else:
                updateData()
            
        elif inputLanjutUpdateData=='2':
            updateData()
        else:
            updateData()

# Menu Hapus / Delete Data
def hapusData():
    print('\n===========================================')
    print('Menu Hapus Data Pasien')
    print('===========================================')
    print('\n1. Hapus Data Pasien')
    print('2. Kembali ke Beranda')
    
    inputUser=input('\nMasukkan Pilihan Menu : ')

    if inputUser=='1':
        hapusDataPasien()
    elif inputUser=='2':
        beranda()
    else:
        hapusData()
        
def hapusDataPasien():
    inputUser=input('\nMasukkan No BPJS Pasien : ')
    if inputUser in isiData:
        print('\nHapus Data Pasien?')
        print('1. Ya')
        print('2. Tidak')
        inputHapusData=input('\nPilih Menu (1/2) : ')
        
        if inputHapusData=='1':
            del isiData[inputUser]
            print('\nData Terhapus!')
            hapusData()
        elif inputHapusData=='2':
            hapusData()
    else:
        print('\nData yang Anda Cari Tidak Ada!')
        hapusData()
        

def keluar():
    global x
    x=False
x=True
while x==True:    
    beranda()
