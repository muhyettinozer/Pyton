class Car:
    def __init__(self, make, model, year, license):
        self.make = make
        self.model = model
        self.year = year
        self.license = license

    def get_string(self):
        return self.year+ ' ' + self.make + ' ' + self.model + ' (' + self.license + ')'

fullstring= []

textname = input("Enter username:")


with open(textname+'.txt', 'r') as reader:
    fullarray = ''.join(reader.readlines()).split("\n\n")[1:]
    for array in fullarray:
        array = array.split('\t')
        make = array[1].lstrip('Make: ').rstrip()
        model = array[2].lstrip('Model: ').rstrip()
        year = array[3].lstrip('Year: ').rstrip()
        license = array[4].lstrip('License: ').rstrip()
        fullstring.append(Car(make, model, year, license).get_string())
    fullstring.sort()
    fullstring=", ".join(fullstring)
    print('ArrayList [',fullstring,']')

