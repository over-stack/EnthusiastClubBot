from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Vacancies(Base):
    __tablename__ = 'Vacancies'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(3000))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime)
    active = Column(Boolean)

    responses = relationship('Responses')
    vacancies_tags = relationship('VacanciesTags')


class Resumes(Base):
    __tablename__ = 'Resumes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(3000), nullable=False)
    last_active_date = Column(DateTime, nullable=False)

    responses = relationship('Responses')
    resumes_tags = relationship('ResumesTags')


class Responses(Base):
    __tablename__ = 'Responses'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('Vacancies.id'))
    resume_id = Column(Integer, ForeignKey('Resumes.id'))
    request_from = Column(Boolean, nullable=False)  # request_from: 0 - resume, 1 - vacancy
    status = Column(Boolean)  # status: null, declined, accepted
    msg = Column(String(1000))


class Tags(Base):
    __tablename__ = 'Tags'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    vacancies_tags = relationship('VacanciesTags')
    resumes_tags = relationship('ResumesTags')


class VacanciesTags(Base):
    __tablename__ = 'VacanciesTags'
    id = Column(Integer, primary_key=True)
    vacancy_id = Column(Integer, ForeignKey('Vacancies.id'))
    tag_id = Column(Integer, ForeignKey('Tags.id'))


class ResumesTags(Base):
    __tablename__ = 'ResumesTags'
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('Resumes.id'))
    tag_id = Column(Integer, ForeignKey('Tags.id'))


# функции
# 1. Создание резюме
# 2. Создание вакансии (можно создать несколько вакансий)
# 3. Удаление резюме (может истечь самостоятельно, если долго не искал работу)
# 4. Удаление вакансии (может истечь самостоятельно, по прошествии определенного количества дней)
# 5. Изменение резюме
# 6. Изменение вакансии
# 7. Поиск вакансии (по названию, по тегам из резюме, ввести теги вручную)
# 8. Поиск резюме (по названию, по тегам вакансии, ввести теги вручную)
#                   если по тегам вакансии, то сначала идет выбор вакансии
#                   в остальных случаях в отклике на резюме выбор вакансии идет в конце
# 9. Отклик на вакансию
# 10. Отклик на резюме
# 11. Подтверждение отклика на вакансию
# 12. Подтверждение отклика на резюме
# 13. Отклонение отклика на вакансию
# 14. Отклонение отклика на реюзме
# 15. Посмотреть вакансии, на которые откликался

# теги пишутся слитно и нижним регистром
# обработка отклика на удаленную вакансию
# сделать так, чтобы нельзя было откликаться 2 раза на одно и то же

# hh.ru: поиск чисто по названию

#  поиск:
#       найти команду
#               по названию
#       найти вакансию
#               АВТОМАТИЧЕСКИ (по названию резюме, по тегам из резюме)
#               ВВЕДИТЕ НАЗВАНИЕ ДОЛЖНОСТИ (по названию вакансии, по названию резюме, по тегам из реюме,
#                                           по тегам вакансий, найденных по названию)
#       найти единомышленника
#               по названию
#               по тегам
#

# теги - это хорошо, но нужно добавить специализацию (взять с hh.ru)

# категории:
#       Большие данные
#           Data Analyst
#           Data Engineer
#           Data Scientist
#       Сайты
#           Frontend
#           Backend
#           Fullstack
#       Дизайн
#       3д графика
#           моделирование
#           рендеринг
#           текстурирование
#       Мобильные приложения
#       Игры
#       Музыка
#       Озвучивание
#       Презентация
#       Видеомонтаж
#       Информационная безопасность
#       Компьютерные приложения
#       Микроконтроллеры
#       Маркетинг
#       Психология
#       Инвестиции/трейдинг
#       Блокчейн
#       Разработка устройств
#       Сценарист
#       Оператор
#       Переводчик
#       Юрист
#       Адвокат
#       Биология/химия/физика/астрономия/геология и многое другое

# 1 frontend / backend
# 2 мобильные приложения
# 3 игры
# 4 аналитика / ML/DL / Big Data
# 5 продвижение
# 6 дизайн / 2D/3D графика
# 7 видеомонтаж / съемка
# 8 музыка / озвучка
# 9 другое

# 1-4 - программирование

# СДЕЛАТЬ СОЦСЕТЬ, ОБЪЕДИНЯЮЩУЮ НЕОБХОДИМЫХ ДРУГ ДРУГУ ЛЮДЕЙ
# ПОИСК ДОПОЛНЯЮЩИХ ПРОФЕССИЯ ДЛЯ АЙТИШНИКОВ В КОМАНДУ

# это просто теги или же стоит заранее продумать категории?

# сервис поиска команды для старапов!
