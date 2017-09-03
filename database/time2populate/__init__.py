from database.paperscraper import paperscraper
import MySQLdb


class time2populate:

    def __init__(self):
        print("Starting time2populate...")

        db = MySQLdb.connect(host="localhost", user="admin", passwd="sdp", db="paper_schema", charset="utf8")
        self.strip(db, True)

    def strip(self, db, save):
        print("Stripping Arion and saving results...")

        ps = paperscraper()

        papers = ps.get_papers()

        # In this loop we iterate through the papers at AUT
        for paper_id, paper_obj in papers.items():

            print("\nGetting the timetables for " + paper_id)

            paper_obj.collect_data()
            timetable = paper_obj.timetable

            print(" - Streams found: " + str(len(timetable)))
            if len(timetable) < 1: continue

            if save:
                print(" - Adding " + paper_id + " to 'paper'")
                self.add_paper_to_db(db, paper_id, paper_obj.name, paper_obj.prescriptor, float(paper_obj.efts),
                                     float(paper_obj.points), int(paper_obj.level))

            # In this loop we iterate through the streams for the current paper
            for stream_id, stream_obj in timetable.items():
                if save:
                    print("   - Adding stream " + stream_id + " to 'stream'")
                    self.add_stream_to_db(db, paper_id, stream_id)

                # In this loop we iterate through the lectures for the current stream
                for lec in stream_obj.get_lectures():
                    if save:
                        print("     - Adding lecture in " + lec.room)
                        self.add_lecture_to_db(db, paper_id, stream_id, lec.room, lec.start, lec.finish, lec.starting,
                                               lec.day)

    def add_paper_to_db(self, db, paper_id, paper_name, paper_desc, efts, points, level):

        statement = ("INSERT INTO paper(paper_id, paper_name, paper_desc, efts, points, level) "
                     "VALUES (%s, %s, %s, %s, %s, %s)")

        try:

            c = db.cursor()
            c.execute(statement, (paper_id, paper_name, paper_desc, str(efts), str(points), str(level)))

            db.commit()
        except Exception as e:
            print(e)
            print("There was an issue. Rolling back changes")
            db.rollback()

        finally:
            c.close()

    def add_stream_to_db(self, db, paper_id, stream_id):

        statement = ("INSERT INTO stream(paper_id, stream_id) "
                     "VALUES (%s, %s)")

        try:

            c = db.cursor()
            c.execute(statement, (paper_id, stream_id))

            db.commit()
        except Exception as e:
            print(e)
            print("There was an issue. Rolling back changes")
            db.rollback()

        finally:
            c.close()

    def add_lecture_to_db(self, db, paper_id, stream_id, room, start_time, end_time, start_date, day):

        statement = ("INSERT INTO lecture(paper_id, stream_id, room, start_time, end_time, start_date, day) "
                     "VALUES (%s, %s, %s, %s, %s, %s, %s)")

        try:

            c = db.cursor()
            c.execute(statement, (paper_id, stream_id, room, start_time.strftime("%H:%M:%S"),
                                  end_time.strftime("%H:%M:%S"), start_date.strftime("%Y-%m-%d"), day))

            db.commit()
        except Exception as e:
            print(e)
            print("There was an issue. Rolling back changes")
            db.rollback()

        finally:
            c.close()


time2populate()
