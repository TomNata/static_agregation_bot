from datetime import datetime
import pytest
from bot.services import get_report, get_data_from_text


@pytest.mark.asyncio
async def test_get_month_report():
    """ Тест на формирование отчета по входным данным в виде
    форматированного текста, период - месяц.
    """
    text = '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-10-31T23:59:00", "group_type": "month"}'

    assert await get_report(text) == {'dataset': [5906586, 5515874],
                                      'labels': ['2022-09-01T00:00:00', '2022-10-01T00:00:00']}


def test_get_day_report():
    """ Тест на формирование отчета по входным данным
    из инлайн клавиатуры, период - день.
    """
    async def get_report(dict_data):
        dict_data = {
            'dt_from': datetime(2022, 3, 1, 0, 0),
            'dt_upto': datetime(2022, 3, 2, 23, 59),
            'group_type': 'day'}

        assert await get_report(dict_data) == {
            'dataset': [213504, 199276],
            'labels': ['2022-03-01T00:00:00', '2022-03-02T00:00:00']
        }


def test_get_hour_report():
    """ Тест на формирование отчета по входным данным в виде
    форматированного текста, период - час.
    """
    async def get_report(text):
        text = '{"dt_from": "2022-02-02T00:00:00", "dt_upto": "2022-02-02T23:59:00", "group_type": "hour"}'
        assert await get_report(text) == {
            'dataset': [8130, 7643, 4361, 8514, 6849, 7847, 6720, 15531, 5842, 8993, 6426, 7839, 7345,
                        11766, 9984, 11290, 10219, 4438, 7330, 7982, 12366, 7867, 11867, 4914],
            'labels': ['2022-02-02T00:00:00', '2022-02-02T01:00:00', '2022-02-02T02:00:00', '2022-02-02T03:00:00',
                       '2022-02-02T04:00:00', '2022-02-02T05:00:00', '2022-02-02T06:00:00', '2022-02-02T07:00:00',
                       '2022-02-02T08:00:00', '2022-02-02T09:00:00', '2022-02-02T10:00:00', '2022-02-02T11:00:00',
                       '2022-02-02T12:00:00', '2022-02-02T13:00:00', '2022-02-02T14:00:00', '2022-02-02T15:00:00',
                       '2022-02-02T16:00:00', '2022-02-02T17:00:00', '2022-02-02T18:00:00', '2022-02-02T19:00:00',
                       '2022-02-02T20:00:00', '2022-02-02T21:00:00', '2022-02-02T22:00:00', '2022-02-02T23:00:00']
        }


@pytest.mark.asyncio
async def test_get_data_from_text():
    """ Тест функции подготовки входных данных в виде произвольного текста.
    """
    text = "Необходимо посчитать суммы всех выплат с 2.02.2022 по 31 марта 2022 по дням."
    assert await get_data_from_text(text) == {"dt_from": "2022-02-02T00:00:00",
                                              "dt_upto": "2022-03-31T23:59:00",
                                              "group_type": "day"}


