import argparse
import sys
import os
import logging
import ConfigParser
import json
import copy
WORKDIR = os.path.realpath(os.path.dirname(sys.argv[0]))


def init_logger(log_file_name, log_base_path=None, log_level=None,
                logger_name=None, print_to_console=None):
    if log_base_path is None:
        log_base_path = r"\var\log"
    if log_level is None:
        log_level = logging.INFO
    if logger_name is None:
        logger_name = 'default'
    if print_to_console is None:
        print_to_console = False
    logger = logging.getLogger(logger_name)
    format_str = '%(asctime)s %(levelname)s\t%(module)s:%(lineno)d: %(message)s'
    formatter = logging.Formatter(format_str)
    log_full_path = os.path.join(log_base_path, log_file_name)
    global_handler = logging.FileHandler(log_full_path)
    global_handler.setFormatter(formatter)
    logger.addHandler(global_handler)
    if print_to_console:
        soh = logging.StreamHandler(sys.stdout)
        soh.setLevel(logging.DEBUG)
        soh.setFormatter(formatter)
        logger.addHandler(soh)
    logger.setLevel(log_level)
    return logger


def parse_cmd_arguments(custom_args):
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-json_db", default="json_db.json",
                        help="json db input for parser")
    args, _ = parser.parse_known_args(custom_args)
    return args


def parse_input_arguments(custom_args):
    """
    parse_input_arguments() -> config_dict: [dict]
    """
    try:
        config = ConfigParser.ConfigParser()
        conf_file = os.path.basename(__file__).split('.py')[0] + '.conf'
        conf_file = os.path.join(WORKDIR, conf_file)
        config.read(conf_file)
        conf_dict = config.__dict__['_sections'].copy()
    except Exception, e:
        conf_dict = {}
        print "Config_dict wasn't found, running without it \n Exception:%s" % e

    args = parse_cmd_arguments(custom_args)
    conf_dict['run'] = {}
    conf_dict['cmd'] = {}
    conf_dict['cmd']['json_db'] = args.json_db
    conf_dict['LOGGER'] = LOGGER
    return conf_dict


def json_2_dict(conf_dict):
    json1_file = open(conf_dict['cmd']['json_db'])
    json1_str = json1_file.read()
    return json.loads(json1_str)


def db_parser(json_db):
    file_list = json_db['files']
    adict = {'sha_list': [], 'file_count': 0, 'oldest': None}
    result_dict = {'exe': copy.deepcopy(adict), 'pdf': copy.deepcopy(adict),
                   'py': copy.deepcopy(adict)}
    for i, afile in enumerate(file_list):
        file_type = afile['file_type']
        file_sha = afile['sha256']
        date = afile['date']
        if file_sha not in result_dict[file_type]['sha_list']:
            result_dict[file_type]['sha_list'].append(file_sha)
            result_dict[file_type]['file_count'] += 1
        if result_dict[file_type]['oldest']:
            if date < result_dict[file_type]['oldest']:
                result_dict[file_type]['oldest'] = date
        else:
            result_dict[file_type]['oldest'] = date

    for file_type, values in result_dict.iteritems():
        pline = "\tfiles_type: %s\toccurrences: %s\toldest_entry: %s" \
                % (file_type, values['file_count'], values['oldest'])
        LOGGER.info(pline)

    return result_dict


def main(custom_args=None):
    conf_dict = parse_input_arguments(custom_args)
    if not conf_dict:
        return 1

    conf_dict['json_db'] = json_2_dict(conf_dict)

    conf_dict['result'] = db_parser(conf_dict['json_db'])

    return 0


if __name__ == '__main__':
    LOGGER = init_logger(os.path.basename(__file__) + '.log',
                         log_base_path='%s' % WORKDIR,
                         print_to_console=True, log_level=logging.DEBUG)
    LOGGER.info('start' + os.path.basename(__file__))
    exit_status = main()
    LOGGER.info('exit status = %s' % exit_status)
    LOGGER.info('end' + os.path.basename(__file__))
    sys.exit(exit_status)