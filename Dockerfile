FROM python:3

RUN git clone https://github.com/manolo2829/manudiiez-test-phase.git

WORKDIR /manudiiez-test-phrase

RUN pip install -r requirements.txt

CMD ["python3", "-m", "unittest"]

