from application import db, models


models.User(user_id=1, first_name='Ashish', last_name='Sheelavantar', email='pluckyashish@gmail.com',
            password='123456').save()
models.User(user_id=2, first_name='Adam', last_name='Zealander', email='zzadam@gmail.com',
            password='whyisthat').save()
models.User(user_id=3, first_name='Mellisa', last_name='Atkins', email='atmellisa@gmail.com',
            password='pa$$w0rd').save()
print("Loaded data into User collection")

models.Course(course_id=101, title="Python", description="Basics of Python language", credits="3", term="Semister 1").save()
models.Course(course_id=102, title="Core Java", description="Intro to Java Programming", credits="5", term="Semister 2").save()
models.Course(course_id=103, title="Docker", description="Basics of Containerisation", credits="3", term="Semister 2").save()
models.Course(course_id=104, title="Angular", description="Intro to Angular", credits="3", term="Semister 3").save()
models.Course(course_id=105, title="React", description="Intro to React", credits="4", term="Semister 3").save()
print("Loaded data into Course collection")


models.Enrollment(user_id=1, course_id=101).save()
models.Enrollment(user_id=1, course_id=102).save()
models.Enrollment(user_id=1, course_id=103).save()
models.Enrollment(user_id=1, course_id=105).save()
models.Enrollment(user_id=2, course_id=102).save()
models.Enrollment(user_id=2, course_id=103).save()
models.Enrollment(user_id=2, course_id=104).save()
models.Enrollment(user_id=2, course_id=105).save()
models.Enrollment(user_id=3, course_id=101).save()
models.Enrollment(user_id=3, course_id=102).save()
models.Enrollment(user_id=3, course_id=103).save()
models.Enrollment(user_id=4, course_id=104).save()
models.Enrollment(user_id=4, course_id=101).save()
models.Enrollment(user_id=4, course_id=102).save()
models.Enrollment(user_id=4, course_id=103).save()
print("Loaded data into Enrollment collection")


def dtype(key, value):
    if type(value) == str:
        return "{0} = '{1}'".format(key, str(value))
    else:
        return "{0} = {1}".format(key, value)

# for document in user_json:
#     row = ','.join(dtype(k, v) for k, v in document.items())
#     print(row)


#for document in user_json:
#    models.User(dtype(k, v) for k, v in document.items())
#models.setup_collections(models.Course, course_json)
#models.setup_collections(models.Enrollment, enrollment_json)