import uuid
from django.utils.text import slugify


def upload_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    try:
        return 'profiles/{0}/{1}'.format(instance.username, filename)
    except:
        return 'misc/{0}'.format(filename)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def generate_unique_slug(table, word):
    original = slugify(word)
    unique = original
    num = 1
    while table.objects.filter(slug=unique).exists():
        unique = '%s-%d' % (original, num)
        num += 1
    return unique


def ckeditor_name_generator(filename):
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return filename