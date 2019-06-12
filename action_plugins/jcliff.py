# from ansible import utils
# import ansible.constants as C
# import ansible.utils.template as template
# from ansible import errors
# from ansible.runner.return_data import ReturnData

from ansible.errors import AnsibleError, AnsibleAction, _AnsibleActionDone

import os
import tempfile

from ansible.plugins.action import ActionBase
from ansible.template import Templar

class ActionModule(ActionBase):

  TRANSFERS_FILES = True

  def _create_remote_copy_args(module_args):
    """remove action plugin only keys"""
    return dict((k, v) for k, v in module_args.items() if k not in ('content', 'decrypt'))

  def writeTemplateResultToFile(self,content):
    tmp = tempfile.NamedTemporaryFile('w',delete=False)
    tmp.writelines(content)
    tmp.close()
    return tmp.name

  def templateFromJinjaToYml(self, templateName, subsystem_values):
    templates = self._loader.path_dwim_relative(self._loader.get_basedir(), 'templates/rules', templateName)
    with open(templates, 'r') as file:
      data = file.read()
    self._templar.set_available_variables(subsystem_values)
    return self.writeTemplateResultToFile(self._templar.template(data))

  def run(self, tmp=None, task_vars=None):
    #tmp_remote_src = self._make_tmp_path()
    #print(str(tmp_remote_src)i)
    templateNameBySubsys = {
      'drivers': 'drivers.j2',
      'datasources': 'datasource.j2',
      'system_props': 'system-properties.j2',
      'deployments': 'deployments.j2'
    }
    subsystems = self._task.args['subsystems']
    for subsys in subsystems:
      for key in subsys.keys():
        if key == 'drivers' or key == 'datasources':
          i = 0
          for subsystem_values in subsys[key]:
            i += 1
            self._transfer_file(self.templateFromJinjaToYml(templateNameBySubsys[key], { "values": subsystem_values }), "/etc/ansible/jcliff/" + key + "-" + str(i) + ".yml")
        if key == 'system_props' or key == 'deployments':
          print(templateNameBySubsys[key])
          self._transfer_file(self.templateFromJinjaToYml(templateNameBySubsys[key], { "values": subsys[key]}), "/etc/ansible/jcliff/" + key + ".yml")

    result = super(ActionModule, self).run(tmp, task_vars)
    result.update(self._execute_module(module_name='jcliff', task_vars=task_vars))
    print("back from module")
    #self._remove_tmp_path(self._connection._shell.tmpdir)
    return result

