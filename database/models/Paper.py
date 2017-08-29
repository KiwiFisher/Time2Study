from database import db, conn, Base

class Paper(db.Model):
    __tablename__ = 'paper'
    paper_id = db.Column('paper_id', db.VARCHAR, primary_key=True)
    paper_name = db.Column('paper_name', db.VARCHAR)
    paper_desc = db.Column('paper_desc', db.VARCHAR)
    efts = db.Column('efts', db.DECIMAL)
    points = db.Column('points', db.DECIMAL)
    level = db.Column('level', db.INTEGER)

    def get_info(paper_id):
        results = conn.execute("SELECT * FROM paper WHERE paper_id='{}'".format(paper_id))

        if results:
            info = {}

            # Add all of the paper info to the results dictionary
            for result in results:
                info['paper_id'] = result['paper_id']
                info['paper_name'] = result['paper_name']
                info['paper_desc'] = result['paper_desc']
                info['efts'] = result['efts']
                info['points'] = result['points']
                info['level'] = result['level']

                lectures = conn.execute("SELECT * FROM lecture WHERE paper_id='{}'".format(paper_id))
                info['streams'] = {}

                for lecture in lectures:
                    if lecture['stream_id'] not in info['streams']:
                        print("MAKE")
                        info['streams'][lecture['stream_id']] = []


                    lec_info = {}
                    lec_info['room'] = lecture['room']
                    lec_info['day'] = str(lecture['day'])
                    lec_info['start_time'] = str(lecture['start_time'])
                    lec_info['end_time'] = str(lecture['end_time'])
                    lec_info['start_date'] = str(lecture['start_date'])

                    info['streams'][lecture['stream_id']].append(lec_info)

            return info

        else:
            return {}
