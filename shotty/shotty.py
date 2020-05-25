import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "foo bar baz"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.placement.get('Affinity', 'I have no affinity for thee!'),
            i.state['Name'],
            str(i.state['Code'])
        )))

if __name__ == '__main__':
    list_instances()
    

    
    