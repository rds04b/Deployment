from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def validate_and_create(self, data):
        print data, "data exists"

        errors = []

        if len(data['name']) < 2:
            print "course name is too short"
            errors.append('course name is too short')
        if len(data['description']) < 2:
            print "discription is too short"
            errors.append('description is too short')

        if errors:
            return(False, errors)
        else:
            new_course = Course.objects.create(
                name=data['name'],
                description=data['description'],
            )
            return (True, new_course)

class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CourseManager()
