from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    company_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    web = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    def dict(self):
        return dict(
            id=self.id,
            first_name=self.first_name,
            last_name=self.last_name,
            company_name=self.company_name,
            city=self.city,
            state=self.state,
            zip=self.zip,
            email=self.email,
            web=self.web,
            age=self.age,
        )