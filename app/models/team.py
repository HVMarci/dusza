from app.connection import fetchone, fetchall, execute


class Team:
    def __init__(self, team_name, description, evfolyam, osztaly, verseny_id=None, id=None):
        self.team_name = team_name
        self.description = description
        self.evfolyam = evfolyam
        self.osztaly = osztaly
        self.verseny_id = verseny_id
        self.id = id

    def __repr__(self):
        return (f"Team(team_name={self.team_name},description={self.description}, evfolyam={self.evfolyam},"
                f"osztaly={self.evfolyam}, verseny_id={self.verseny_id}, id={self.id}")

    @staticmethod
    def create_from_row(row):
        return Team(row['team_name'], row['description'], row['evfolyam'], row['osztaly'], row['verseny_id'], row['id'])

    @staticmethod
    def find_by_id(id):
        query = '''
        SELECT `id`, `team_name`, `description`, `evfolyam`, `osztaly`, `verseny_id` FROM `teams`
        WHERE `id` = %s;
        '''

        return Team.create_from_row(fetchone(query, (id,)))

    @staticmethod
    def find_by_verseny(verseny_id):
        query = '''
                SELECT `id`, `team_name`, `description`, `evfolyam`, `osztaly`, `verseny_id` FROM `teams`
                WHERE `verseny_id` = %s;
                '''

        return [Team.create_from_row(row) for row in fetchall(query, (verseny_id,))]

    @staticmethod
    def find_all():
        query = '''
        SELECT `id`, `team_name`, `description`, `evfolyam`, `osztaly`, `verseny_id` FROM `teams`;
        '''

        return [Team.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def delete(id):
        query = '''
            DELETE FROM `teams`
            WHERE `id` = %s;
        '''

        execute(query, (id,))

    @staticmethod
    def save(team):
        if team.id:
            query = '''
                    UPDATE `teams`
                    SET `team_name` = %s, `description` = %s, `verseny_id` = %s, `evfolyam` = %s, `osztaly` = %s
                    WHERE `id` = %s;
                '''

            execute(query, (team.team_name, team.description, team.verseny_id, team.evfolyam, team.osztaly, team.id))
        else:
            query = '''
                    INSERT INTO `teams`(`team_name`, `description`, `verseny_id`, `evfolyam`, `osztaly`)
                    VALUES (%s, %s, %s, %s, %s);
                '''

            team.id = execute(query, (team.team_name, team.description, team.verseny_id, team.evfolyam, team.osztaly))

        return team
