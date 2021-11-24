from worker import Worker
from unittest import TestCase, main

class WorkerTests(TestCase):
    def test_if_the_worker_is_initialized_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy, msg="The energy must be equal to 10")
        self.assertEqual(0, worker.money)
    
    def test_if_the_worker_energy_increments_after_rest(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_if_an_error_is_raised_when_the_energy_is_less_than_or_equal_to_zero(self):
        worker = Worker("Test", 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        
        self.assertEqual("Not enough energy.", str(ex.exception))
    
    def test_if_the_worker_money_are_increased_by_his_salary_when_he_works(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)
    
    def test_if_the_worker_energy_is_decreased_after_work(self):
        worker = Worker("Test", 100, 10)
        worker.work()
        self.assertEqual(9, worker.energy)
    
    def test_if_the_worker_method_get_info_returns_the_correct_msg(self):
        worker = Worker("Test", 100, 10)
        msg = worker.get_info()
        self.assertEqual("Test has saved 0 money.", msg)
if __name__ == "__main__":
    main()        



