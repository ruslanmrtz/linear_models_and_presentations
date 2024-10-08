from sqlalchemy import TIMESTAMP, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .config import Base, SessionLocal


class Member(Base):
    __tablename__ = "members"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True, name="memid")
    surname = Column(String)
    first_name = Column(String, name="firstname")
    address = Column(String)
    zipcode = Column(String)
    telephone = Column(String)

    recommended_by_id = Column(
        Integer, ForeignKey("cd.members.memid"), name="recommendedby"
    )
    recommended_by = relationship("Member", remote_side=[id])

    join_date = Column(TIMESTAMP, name="joindate")


class Facility(Base):
    __tablename__ = "facilities"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True, name="facid")
    name = Column(String)
    member_cost = Column(Float, name="membercost")
    guest_cost = Column(Float, name="guestcost")
    initial_outlay = Column(Float, name="initialoutlay")
    monthly_maintenance = Column(Float, name="monthlymaintenance")


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": "cd"}

    id = Column(Integer, primary_key=True, name="bookid")

    facility_id = Column(
        Integer, ForeignKey("cd.facilities.facid"), primary_key=True, name="facid"
    )
    facility = relationship("Facility")

    member_id = Column(
        Integer, ForeignKey("cd.members.memid"), primary_key=True, name="memid"
    )
    member = relationship("Member")

    start_time = Column(TIMESTAMP, name="starttime")
    slots = Column(Integer)


if __name__ == '__main__':
    session = SessionLocal()
    results = (session.query(Booking)\
                     .join(Member)\
                     .filter(Member.surname == 'Smith')\
                     .limit(3)
                     .all())

    for result in results:
        print(result.member.first_name, result.member.surname,
              result.start_time)
