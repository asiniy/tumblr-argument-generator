#!/usr/bin/env python

from random import choice

intro = [
	'burn in hell',
	'check your privilege',
	'fuck you',
	'please die',
	'rot in hell',
	'screw you',
	'shut the fuck up',
	'shut up',
]
description = [
	'deluded',
	'fucking',
	'god damn',
	'judgemental',
	'worthless',
]
marginalized = [
	[
		'activist',
		'agender',
		'appearance',
		'asexual',
		'asian',
		'attractive',
		'bi',
		'bigender',
		'black',
		'celestial',
		'chubby',
		'closet',
		'color',
		'curvy',
		'dandy',
		'deathfat',
		'demi',
		'demiromantic',
		'differently abled',
		'disabled',
		'diversity',
		'dysphoria',
		'ethnic',
		'ethnicity',
		'fat love',
		'fat',
		'fatist',
		'fatty',
		'female',
		'feminist',
		'femme',
		'genderfluid',
		'genderfuck',
		'genderless',
		'genderqueer',
		'hair',
		'height',
		'indigenous',
		'intersectionality',
		'invisible',
		'kin',
		'lesbianism',
		'little person',
		'marginalized',
		'minority',
		'multigender',
		'non-gender',
		'non-white',
		'obesity',
		'other',
		'otherkin',
		'pansexual',
		'polyamorous',
		'polygender',
		'polyromantic',
		'privilege',
		'prosthetic',
		'queer',
		'radfem',
		'skinny',
		'smallfat',
		'stretchmark',
		'thin',
		'third-gender',
		'trans*',
		'transgender',
		'transman',
		'transwoman',
		'trigger',
		'two-spirit',
		'womyn',
	],
    [
		'chauvinistic',
		'misogynistic',
		'nphobic',
		'oppressive',
		'phobic',
		'shaming',
	    'denying',
	    'discriminating',
	    'hypersexualizing',
	    'intolerant',
	    'racist',
	    'sexualizing',
	]]
privileged = [
	[
		'able-bodied',
		'appearance',
		'attractive',
		'binary',
		'cis',
		'cisgender',
		'cishet',
		'hetero',
		'male',
		'rich',
		'smallfat',
		'thin',
		'white',
	],
	[
		'ableist',
		'classist',
		'normative',
		'overprivileged',
		'patriarch',
		'sexist',
	    'privileged',
    ]]
finisher = [
	'asshole',
	'bigot',
	'oppressor',
	'piece of shit',
	'rapist',
	'scum',
	'shitlord',
	'subhuman',
]

print('{intro}, you {description} {marginalized[0]}-{marginalized[1]}, {privileged[0]}-{privileged[1]} {finisher}'.format(
	intro=choice(intro),
	description=choice(description),
	marginalized=[
		choice(marginalized[0]),
		choice(marginalized[1]),
	],
	privileged=[
		choice(privileged[0]),
		choice(privileged[1]),
	],
	finisher=choice(finisher)
).upper())
