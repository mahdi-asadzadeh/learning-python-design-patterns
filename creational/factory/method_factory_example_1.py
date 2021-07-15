from abc import ABC, abstractmethod


# Product
class Section(ABC):

    @abstractmethod
    def describe(self):
        pass


class PersonalInformationSection(Section):
    def describe(self):
        print('personal information section.')
    

class AlbumSection(Section):
    def describe(self):
        print('album section.')


class PublicationSection(Section):
    def describe(self):
        print('publication section.')


# Creator
class Profile(ABC):
    def __init__(self):
        self.sections = []
        self.create_profile()
    
    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        for section in self.sections:
            section.describe()
    
    def add_sections(self, section):
        self.sections.append(section)


class LinkedIn(Profile):
    def create_profile(self):
        self.add_sections(PersonalInformationSection())
        self.add_sections(AlbumSection())
        self.add_sections(PublicationSection())


class Instagram(Profile):
    def create_profile(self):
        self.add_sections(PersonalInformationSection())
        self.add_sections(AlbumSection())
        self.add_sections(PublicationSection())


# Client
if __name__ == '__main__':
    class_name = input('Enter: [LinkedIn, Instagram] : ')
    profile = eval(class_name)()
    profile.get_sections()
