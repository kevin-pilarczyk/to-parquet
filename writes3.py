unload_query = """
            UNLOAD ( $$ {select_query} $$)
            TO '{s3_unload_path}'
            iam_role '{iam_role}'
            {unload_options};
            """.format(select_query=select_query,
                       s3_unload_path=self.s3_unload_path,
                       iam_role=self.iam_role,
                       unload_options=self.unload_options)
self.hook.run(unload_query, self.autocommit)
self.log.info("UNLOAD command complete...")