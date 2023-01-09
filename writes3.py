unload_query = """
            UNLOAD ( $$ {select_query} $$)
            TO '{s3_unload_path}'
            iam_role '{iam_role}'
            {unload_options};
            """.format(select_query=select_query,
                       s3_unload_path=s3_unload_path,
                       iam_role=iam_role,
                       unload_options=unload_options)
hook.run(unload_query, autocommit)
log.info("UNLOAD command complete...")