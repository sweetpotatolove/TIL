from django.db import models
from teachers.models import Teacher


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    main_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # assistant_teachers = models.ManyToManyField(Teacher)
    assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses")
    # assistant_teachers = models.ManyToManyField(Teacher, related_name="assistant_courses", through='CourseInfo')
    # assistant_teachers = models.ManyToManyField(Teacher, 
    #                                             related_name="assistant_courses", 
    #                                             symmetrical=False
    #                                             )


# 참조 : Through 참고 
# N:M 관계에서 추가적인 정보를 저장하고 싶은 경우에는 중개 모델을 사용할 수 있음
# 이 경우에는 중개 모델을 정의하고 through 옵션에 중개 모델을 지정하면 됨
# 중개모델에는 반드시 관계 설정을 원하는 두 모델을 ForeignKey로 지정해야 함
# class CourseInfo(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Course 모델과의 관계
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Teacher 모델과의 관계
#     max_student = models.PositiveIntegerField(default=20)
#     is_nessary = models.BooleanField(default=False)
    
#     class Meta:
#         unique_together = ('course', 'teacher')
