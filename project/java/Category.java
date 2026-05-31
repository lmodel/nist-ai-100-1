package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A category within an AI RMF Core function (e.g., "GOVERN 1:
Policies, processes, procedures, and practices ... are in place,
transparent, and implemented effectively"). Categories group
related subcategories.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Category extends NamedThing {

  private String categoryId;
  private String outcome;
  private List<Subcategory> subcategories;


}