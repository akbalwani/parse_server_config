import csv,os
import xml.etree.ElementTree as ET
import time

main_data_file = 'systemConfiguration_55_old.xml'

# Parse the XML file
tree = ET.parse('data/'+main_data_file)
#loading all config options 
configurationModel = tree.getroot()



def export_CNP():

    # print(configurationModel)
    #opening csv to write all of these
    csv_file_ConfigurationNameProtocol = open('result/CNP_'+os.path.splitext(main_data_file)[0]+'.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file_ConfigurationNameProtocol)
    csv_writer.writerow(['Name','protocol'])
    for cnp in configurationModel.findall('ConfigurationNameProtocol'):
        name = cnp.find('name').text
        protocol = cnp.find('protocol').text
        # print(cnp.find('name').text)
        # print(cnp.find('protocol').text)

        csv_writer.writerow([name,protocol])

    #closing csv_file_ConfigurationNameProtocol file
    csv_file_ConfigurationNameProtocol.close()

#Getting all config files

def export_configurations():
    csv_file_Configurations = open('result/configurations_'+os.path.splitext(main_data_file)[0]+'.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file_Configurations)
    csv_writer.writerow(['Name','filePath','fileFormat'])
    for config in configurationModel.findall('configuration'):
        # print(config.find('name').text)
        name = config.find('name').text
        filepath = config.find('filePath').text
        fileFormat = config.find('filePath').text
        csv_writer.writerow([name,filepath,fileFormat])

    csv_file_Configurations.close()



def export_options():
    #loading all options from system configuration xml file
    option = tree.getroot().find('options').find('option')
    csv_file_options = open('result/options_'+os.path.splitext(main_data_file)[0]+'.csv', 'w', newline='')
    csv_writer = csv.writer(csv_file_options)
    csv_writer.writerow(["description", "name", "cluster_node", "profile", "value","read_only", 
                        "is_disabled", "is_specified", "encrypted","export_configuration", "export_key", "export_path"])

    for option_item in option.findall('optionItem'):
        description_element = option_item.find('description')
        description  =description_element.text if description_element is not None else 'NO value'
        name_element = option_item.find('name')
        name = name_element.text if name_element is not None else 'NO value'
        cluster_node_element = option_item.find('clusterNode')
        cluster_node = cluster_node_element.text if cluster_node_element is not None else 'NO value'
        profile_element = option_item.find('profile')
        profile = profile_element.text if profile_element is not None else 'NO value'

        # Handle the 'value' element
        value_element = option_item.find('value')
        value = value_element.text if value_element is not None else 'NO value'

        # Handle other elements similarly
        read_only_element = option_item.find('readOnly')
        read_only = read_only_element.text if read_only_element is not None else 'NO value'

        is_disabled_element = option_item.find('isDisabled')
        is_disabled = is_disabled_element.text if is_disabled_element is not None else 'NO value'

        is_specified_element = option_item.find('isSpecified')
        is_specified = is_specified_element.text if is_specified_element is not None else 'NO value'

        encrypted_element = option_item.find('encrypted')
        encrypted = encrypted_element.text if encrypted_element is not None else 'NO value'
        export_rules = option_item.find('exportRules')
        if export_rules is not None:
            export_rule = export_rules.find('exportRule')
            
            try:
                export_configuration = export_rule.find('configuration').text
            except AttributeError:
                export_configuration = 'NO value'
            
            try:
                export_key = export_rule.find('exportKey').text
            except AttributeError:
                export_key = 'NO value'
            
            try:
                export_path = export_rule.find('exportPath').text
            except AttributeError:
                export_path = 'NO value'
        else:
            export_configuration = 'NO value'
            export_key = 'NO value'
            export_path = 'NO value'

        csv_writer.writerow([
                description, name, cluster_node, profile, value,
                read_only, is_disabled, is_specified, encrypted,
                export_configuration, export_key, export_path
            ])

    csv_file_options.close()


export_CNP()
export_configurations()
export_options()