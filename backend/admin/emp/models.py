from django.db import models

# Create your models here.


class EmpVo(models.Model):
    use_in_migrations = True
    emp_no = models.AutoField(primary_key = True)
    ename = models.TextField()
    job = models.TextField()
    mgr = models.IntegerField()
    hire_date = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField()
    dept_no = models.ForeignKey("dept.DeptVo", on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'emp'

    def __str__(self):
        return f'[{self.pk}] {self.emp_no}'