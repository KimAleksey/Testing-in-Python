import pytest

from dags.utils_for_orchestration.utils_str import generate_insert_into_for_row

class TestGenerateInsertIntoForRow:
    def test_valid_input(self):
        result = generate_insert_into_for_row(
            schema="public",
            table="table1",
            columns="(col1, col2)",
            placeholders="%(col1)s, %(col2)s"
        )
        assert result == 'INSERT INTO "public"."table1" ((col1, col2)) VALUES (%(col1)s, %(col2)s);'

    def test_empty_table(self):
        with pytest.raises(ValueError):
            generate_insert_into_for_row(
                schema="public",
                table="",
                columns="(col1, col2)",
                placeholders="%(col1)s, %(col2)s"
            )

    def test_empty_columns(self):
        with pytest.raises(ValueError):
            generate_insert_into_for_row(
                schema="public",
                table="table1",
                columns="",
                placeholders="%(col1)s, %(col2)s"
            )

    def test_empty_placeholders(self):
        with pytest.raises(ValueError):
            generate_insert_into_for_row(
                schema="public",
                table="table1",
                columns="(col1, col2)",
                placeholders=""
            )

    def test_schema_not_str(self):
        with pytest.raises(TypeError):
            generate_insert_into_for_row(
                schema=123,
                table="table1",
                columns="(col1, col2)",
                placeholders="%(col1)s, %(col2)s"
            )

    def test_table_not_str(self):
        with pytest.raises(TypeError):
            generate_insert_into_for_row(
                schema="public",
                table=123,
                columns="(col1, col2)",
                placeholders="%(col1)s, %(col2)s"
            )

    def test_columns_not_str(self):
        with pytest.raises(TypeError):
            generate_insert_into_for_row(
                schema="public",
                table="table1",
                columns=123,
                placeholders="%(col1)s, %(col2)s"
            )

    def test_placeholders_not_str(self):
        with pytest.raises(TypeError):
            generate_insert_into_for_row(
                schema="public",
                table="table1",
                columns="(col1, col2)",
                placeholders=123
            )
