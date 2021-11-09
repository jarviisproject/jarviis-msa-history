from django.db import models

# Create your models here.


class DeptVo(models.Model):
    use_in_migrations = True
    dept_no = models.AutoField(primary_key = True)
    dname = models.TextField()
    loc = models.TextField()

    class Meta:
        managed = True
        db_table = 'dept'

    def __str__(self):
        return f'[{self.pk}] {self.dept_no}'