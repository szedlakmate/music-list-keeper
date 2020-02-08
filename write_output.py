def write_to_file(output_file_name, titles):
    output_dir = 'my_lists'

    with open('%s/%s' % (output_dir, output_file_name), 'w') as result_file:
        print('\n\n\nOutput: %s' % output_file_name)
        result_file.write('Number of found musics:%i\n\n' % len(titles))

        for title in titles:
            print(title)
            result_file.write(title + "\n")
