from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Fast")

    def test_constructor(self):
        with self.assertRaises(ValueError) as er:
            team = Team("Team123")
        self.assertEqual("Team Name can contain only letters!", str(er.exception))

        self.assertEqual("Fast", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_add_member(self):
        msg = self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        self.assertEqual({"Ivan": 42, "Dimitar": 38}, self.team.members)
        self.assertEqual("Successfully added: Ivan, Dimitar", msg)
        msg = self.team.add_member(**{"Ivan": 35})
        self.assertEqual({"Ivan": 42, "Dimitar": 38}, self.team.members)
        self.assertEqual("Successfully added: ", msg)

    def test_remove_member(self):
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        msg = self.team.remove_member("Ivan")
        self.assertEqual("Member Ivan removed", msg)
        self.assertEqual({"Dimitar": 38}, self.team.members)
        msg = self.team.remove_member("Petar")
        self.assertEqual("Member with name Petar does not exist", msg)
        self.assertEqual({"Dimitar": 38}, self.team.members)

    def test_gt(self):
        other_team = Team("Slow")
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        other_team.add_member(**{"Petar": 42})
        result = self.team > other_team
        self.assertEqual(True, result)
        result = other_team > self.team
        self.assertEqual(False, result)

    def test_len(self):
        self.assertEqual(0, len(self.team))
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        self.assertEqual(2, len(self.team))

    def test_add(self):
        other_team = Team("Slow")
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        other_team.add_member(**{"Petar": 42})
        new_team = self.team + other_team
        self.assertEqual("FastSlow", new_team.name)
        self.assertEqual({"Ivan": 42, "Dimitar": 38, "Petar": 42}, new_team.members)

    def test_add_with_equal_members(self):
        other_team = Team("Slow")
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        other_team.add_member(**{"Petar": 42, "Ivan": 42})
        new_team = self.team + other_team
        self.assertEqual("FastSlow", new_team.name)
        self.assertEqual({"Ivan": 42, "Dimitar": 38, "Petar": 42}, new_team.members)

    def test_str(self):
        self.team.add_member(**{"Ivan": 42, "Dimitar": 38})
        msg = str(self.team)
        expected_msg = "Team name: Fast\nMember: Ivan - 42-years old\nMember: Dimitar - 38-years old"
        self.assertEqual(expected_msg, msg)


if __name__ == "__main__":
    main()
