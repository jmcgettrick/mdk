<?php
/**
 * Moodle Development Kit
 *
 * Copyright (c) 2012 Frédéric Massart - FMCorz.net
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * http://github.com/FMCorz/mdk
*/

echo "<h2>Moodle Development Kit</h1>";
echo "<ul>";

$path = getcwd();
$dirs = scandir($path);
foreach ($dirs as $dir) {
    if ($dir == '.' || $dir == '..' || !is_dir($path . '/' . $dir)) {
        continue;
    }
    print "<li><a href='$dir'>$dir</a></li>";
}

echo "</ul>";
